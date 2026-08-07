from hashlib import md5
from sys import maxsize
from glob import glob
from os import path as _path

paths = ["advent_of_code/2018/input.txt", "2018/input.txt", "input.txt"]
for path in paths:
    if _path.exists(path):
        with open(path, "r") as f:
            problem_data = f.read().strip()  # type: str

def throw():
    raise Exception("Unreachable code detected")


def get_md5_hash(s: str):
    return md5(s.encode()).hexdigest()
