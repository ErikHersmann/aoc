from hashlib import md5
from sys import maxsize
from glob import glob
from os import path as _path

paths = ["advent_of_code/2017/input.txt", "2017/input.txt", "input.txt"]
for path in paths:
    if _path.exists(path):
        with open(path, "r") as f:
            problem_data = f.read().strip()  # type: str
        with open(path, "r") as f:
            unstripped_problem_data = f.read()

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
TRANSFORM = {
    "left": {LEFT: DOWN, RIGHT: UP, DOWN: RIGHT, UP: LEFT},
    "right": {LEFT: UP, RIGHT: DOWN, DOWN: LEFT, UP: RIGHT},
    "flip": {LEFT: RIGHT, RIGHT: LEFT, UP: DOWN, DOWN: UP}
}




def throw():
    raise Exception("Unreachable code detected")


def get_md5_hash(s: str):
    return md5(s.encode()).hexdigest()
