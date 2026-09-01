from lib import CACHE_PATH
from json import load, dump, dumps
from inspect import getsourcelines
from copy import deepcopy
from os import path
from itertools import product
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
        Self.BITWISE_OPERATORS = [
            "&",
            "|",
            "^",
            "~",
            "<<",
            ">>",
        ]
        Self.NUMERICAL_OPERATORS = [
            "%",
            "+",
            "-",
            "*",
            "//",
        ]
        Self.COMPARISON_OPERATORS = [
            ">",
            "<",
            "==",
            "!=",
            "=>",
            "<=",
        ]
        Self.NUMBERS = [str(c) for c in range(10)]
        Self.PARENTHESIS = [
            "(",
            ")",
        ]
        Self.TOKENS = []
        Self.TOKENS.append(Self.SYMBOL_NAME)
        Self.TOKENS.extend(Self.PARENTHESIS)
        Self.TOKENS.extend(Self.NUMBERS)
        Self.TOKENS.extend(Self.OPERATOR_TOKENS)
        Self.OPERATOR_TOKENS = []
        Self.OPERATOR_TOKENS.extend(Self.BITWISE_OPERATORS)
        Self.OPERATOR_TOKENS.extend(Self.NUMERICAL_OPERATORS)
        Self.OPERATOR_TOKENS.extend(Self.COMPARISON_OPERATORS)
        Self.START_TOKENS = [Self.SYMBOL_NAME, "-", "~", "("]
        Self.START_TOKENS.extend(Self.NUMBERS)
        Self.END_TOKENS = [Self.SYMBOL_NAME, ")"]
        Self.END_TOKENS.extend(Self.NUMBERS)

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

    def __fast_check_valid_solution__(Self, solution: str) -> bool:
        if solution[0] not in Self.START_TOKENS:
            return False
        if solution[-1] not in Self.END_TOKENS:
            return False
        if Self.SYMBOL_NAME not in solution:
            return False
        return True

    def __dp_internal__(Self, expression: list, max_length: int):
        if Self.__get_expression_length__(expression) >= max_length:
            if Self.__validate_expression__(expression):
                Self.__dp_solution_set__.add(expression)
            return
        for char in Self.__get_valid_next_char_set__(expression):
            Self.__dp_internal__(Self, expression + char, max_length)

    def __validate_expression__(Self, expression):
        # TODO: Remove this method as we are technically always valid: because of the construction process of our string
        try:
            eval(f"lambda x: {"".join(expression)}")
            return True
        except:
            return False

    def __get_valid_next_char_set__(Self, expression):
        next_chars = []
        last_char = expression[-1] if len(expression) else "("
        if last_char == "(":
            return Self.START_TOKENS
        if last_char in Self.OPERATOR_TOKENS:
            # TODO: Handle intersection between START_TOKENS and OPERATOR_TOKENS
            return Self.START_TOKENS
        if last_char in Self.NEUTRAL_TOKENS:
            pass
            next_chars.append(")")
        if last_char in Self.END_TOKENS:
            next_chars.extend(Self.OPERATOR_TOKENS)
            if (expression.count("(") - expression.count(")")) <= 0:
                next_chars.remove(")")
            return next_chars
        raise Exception("Unreachable code")

    def dynamic_programming_solve(Self):
        if Self.optimal:
            return
        upper_bound = Self.__get_solution_length__()
        bound = 1
        solutions = []
        print(f"Solving for: {Self.alias}")
        while len(solutions) == 0:
            Self.__dp_solution_set__ = set()
            Self.__dp_internal__([], bound)
            bound += 1
            if Self.debug:
                print(f"New lower bound: {bound}\tUpper bound: {upper_bound}")
            if bound == upper_bound:
                print(f"Didn't find a new solution, old solution must be optimal")
                break
        else:
            Self.solutions = solutions
            print(f"Found new solution")
        Self.__cleanup_suboptimal_solutions__()
        Self.optimal = True
        Self.__sync_with_cache__()

    def enumeration_solve(Self):
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
            for brute_force_solution in product(Self.TOKENS, repeat=bound):
                if not Self.__fast_check_valid_solution__(brute_force_solution):
                    continue
                try:
                    brute_force_solution = f"lambda x: {''.join(brute_force_solution)}"
                    l = eval(brute_force_solution)
                    if Self.__verify_mapping__(l):
                        solutions.append(brute_force_solution)
                        if (
                            Self.__get_solution_length__(len(Self.solutions) - 1)
                            == bound
                        ):
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
        Self.__cleanup_suboptimal_solutions__()
        Self.optimal = True
        Self.__sync_with_cache__()

    def __verify_mapping__(Self, function):
        for source, target in Self.mapping:
            if function(source) != target:
                return False
        return True

    def __cleanup_suboptimal_solutions__(Self):
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

    def __get_expression_length__(Self, expression: list):
        return sum([len(a) for a in expression])

    def __get_solution_length__(Self, idx=0):
        if idx >= len(Self.solutions):
            idx = 0
        return len(Self.solutions[idx].replace("lambda x: ", "").strip())

    def __deserialize_from(Self, copy_from):
        Self.optimal = copy_from["optimal"]
        Self.solutions = copy_from["solutions"]
