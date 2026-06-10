from math import sqrt, ceil
from collections import defaultdict


from functools import reduce
from math import sqrt


# Source - https://stackoverflow.com/a/19578818
# Posted by Steinar Lima, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-10, License - CC BY-SA 4.0


def factors(n):
    """
    I was too stupid to implement this myself, I guess this is considered cheating xD
    """
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


puzzle_input = 29000000


def main(is_part_one: bool):
    if is_part_one:
        for candidate in range(1, puzzle_input):
            if sum(factors(candidate)) >= puzzle_input//10:
                return candidate
    dispose = defaultdict(lambda: 50)
    for candidate in range(1, puzzle_input):
        s = 0
        for fact in [fact for fact in factors(candidate) if dispose[fact] > 0]:
            s += fact*11
            dispose[fact] -= 1
        if s >= puzzle_input:
            return candidate


print(f"Part 1: {main(True)}")
print(f"Part 2: {main(False)}")
