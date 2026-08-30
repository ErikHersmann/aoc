from lib import CACHE_PATH
from json import load, dump, dumps
from inspect import getsourcelines
from copy import deepcopy
from os import path
from itertools import combinations_with_replacement, product
import warnings


warnings.filterwarnings("ignore")


class mapping_object:
    def __init__(Self, source_values: list, function, alias: str):
        Self.alias = alias
        Self.mapping = [(val, function(val)) for val in source_values]
        Self.optimal = False
        deserialized_lambda = ",".join(
            getsourcelines(function)[0][0].split(",")[1:-1]
        ).strip()
        Self.solutions = [deserialized_lambda]
        Self.__sync_with_cache__()
        Self.debug = True
        Self.SYMBOL_NAME = "x"
        numbers = [str(c) for c in range(10)]
        Self.VALID_TOKENS = [
            Self.SYMBOL_NAME,
            "%",
            "&",
            "|",
            "^",
            "~",
            "<<",
            ">>",
            "+",
            "-",
            "*",
            ">",
            "<",
            "==",
            "!=",
            "=>",
            "<=",
            "//",
            # "(",
            # ")"
            # " ",
        ]
        Self.VALID_TOKENS.extend(numbers)
        Self.VALID_START_TOKENS = [
            Self.SYMBOL_NAME,
            "-",
            "~",
            "*",
            "("
        ]
        Self.VALID_START_TOKENS.extend(numbers)
        Self.VALID_END_TOKENS = [
            Self.SYMBOL_NAME,
            ")"
        ]
        Self.VALID_END_TOKENS.extend(numbers)

    def multi_heuristic_search(Self, timeout):
        if Self.optimal:
            return
        pass

    def heuristic_placeholder(Self):
        # TODO: We have to update best known lower and upper bounds from this to "cache results"
        # TODO: Decent time solution
        raise Exception("Not implemented yet")

    def rule_based_search(Self):
        # Maybe a strategic rule-based search
        raise Exception("Not implemented yet")

    def genetic_algorithm(Self):
        raise Exception("Not implemented yet")

    def simulated_annealing(Self):
        raise Exception("Not implemented yet")

    def fast_check_valid_solution(Self, solution: str) -> bool:
        if solution[0] not in Self.VALID_START_TOKENS:
            return False
        if solution[-1] not in Self.VALID_END_TOKENS:
            return False
        if Self.SYMBOL_NAME not in solution:
            return False
        return True

    def solve(Self):
        """Naive brute force implementation to get some reference results for small input cases
           TODO: using AST we try out valid token combos that would save characters
           TODO: Check last character and only allow certain characters based on that or string position

        Args:
            Self (_type_): _description_
        """
        if Self.optimal:
            return
        upper_bound = Self.__get_solution_length__()
        bound = 1
        solutions = []
        print(f"Solving for: {Self.alias}")
        while len(solutions) == 0:
            for brute_force_solution in product(Self.VALID_TOKENS, repeat=bound):
                if not Self.fast_check_valid_solution(brute_force_solution):
                    continue
                try:
                    brute_force_solution = f"lambda x: {''.join(brute_force_solution)}"
                    l = eval(brute_force_solution)
                    if Self.verify_mapping(l):
                        solutions.append(brute_force_solution)
                        if (
                            Self.__get_solution_length__(len(Self.solutions) - 1)
                            == bound
                        ):
                            print(f"Found new solution, exiting early")
                            break
                except:
                    continue
            bound += 1
            if Self.debug:
                print(f"New lower bound: {bound}")
            if bound == upper_bound:
                print(f"Didn't find a new solution, old solution must be optimal")
                break
        else:
            Self.solutions = solutions
            print(f"Found new solution")
        Self.__cleanup_suboptimal_solutions()
        Self.optimal = True
        Self.__sync_with_cache__()

    def verify_mapping(Self, function):
        for source, target in Self.mapping:
            if function(source) != target:
                return False
        return True

    def __cleanup_suboptimal_solutions(Self):
        best = 1000
        indexed_solutions = list(enumerate(Self.solutions))
        for idx, solution in indexed_solutions:
            best = min(best, Self.__get_solution_length__(idx))
        for idx, solution in indexed_solutions[::-1]:
            if Self.__get_solution_length__(idx) > best:
                Self.solutions.pop(idx)

    def __sync_with_cache__(Self):
        if not path.exists(CACHE_PATH):
            with open(CACHE_PATH, "w") as f:
                f.write()
        with open(CACHE_PATH, "r") as f:
            try:
                contents = load(f)
            except:
                contents = []
        for idx, mapping in enumerate(contents):
            if Self.__mappings_equal__(mapping):
                cached_best, local_best = (
                    mapping["length"],
                    Self.__get_solution_length__(),
                )
                if cached_best > local_best:
                    contents[idx] = Self.__serialize__()
                    break
                elif cached_best == local_best:
                    Self.solutions = list(
                        set(mapping["solutions"]).union(set(Self.solutions))
                    )
                    Self.optimal = mapping["optimal"]
                    contents[idx] = Self.__serialize__()
                    break
                else:
                    Self.__deserialize_from(mapping)
                    return
        else:
            contents.append(Self.__serialize__())
        with open(CACHE_PATH, "w") as f:
            dump(contents, f)

    def __mappings_equal__(Self, other):
        if "mapping" not in other:
            return False
        other_mapping = other["mapping"]
        for idx, kvp in enumerate(Self.mapping):
            if other_mapping[idx][0] != kvp[0] or other_mapping[idx][1] != kvp[1]:
                return False
        return True

    def __serialize__(Self):
        value = {
            "alias": Self.alias,
            "mapping": Self.mapping,
            "optimal": Self.optimal,
            "solutions": Self.solutions,
            "length": Self.__get_solution_length__(),
        }
        return value

    def __get_solution_length__(Self, idx=0):
        if idx >= len(Self.solutions):
            idx = 0
        return len(Self.solutions[idx].replace("lambda x: ", "").strip())

    def __deserialize_from(Self, copy_from):
        Self.optimal = copy_from["optimal"]
        Self.solutions = copy_from["solutions"]
