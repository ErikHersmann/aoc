from hashlib import md5
from sys import maxsize

try:
    with open("input.txt", "r") as f:
        # Some description
        problem_data = f.read().strip()  # type: str
except:
    with open("advent_of_code/2018/input.txt", "r") as f:
        # Some description
        problem_data = f.read().strip()  # type: str


def throw():
    raise Exception("Unreachable code detected")


def get_md5_hash(s: str):
    return md5(s.encode()).hexdigest()
