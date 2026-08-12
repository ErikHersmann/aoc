from hashlib import md5
from sys import maxsize
from glob import glob
from os import path as _path
from math import sqrt

paths = ["advent_of_code/2017/input.txt", "2017/input.txt", "input.txt"]
for path in paths:
    if _path.exists(path):
        with open(path, "r") as f:
            problem_data = f.read().strip()
        with open(path, "r") as f:
            unsanitized_problem_data = f.read()



def flip_square_string_90_degrees_right(string: str):
    assert sqrt(len(string.replace("\n", ""))).is_integer()
    columns = string.splitlines()[::-1]
    output = ""
    for index in range(len(columns)):
        output += "".join([col[index] for col in columns]) + "\n"
    output = output.strip("\n")
    return output

def flip_square_string_180_degrees_along_horizontal_axis(string: str):
    assert sqrt(len(string.replace("\n", ""))).is_integer()
    rows = string.splitlines()[::-1]
    return "\n".join(rows)

def flip_square_string_180_degrees_along_vertical_axis(string: str):
    assert sqrt(len(string.replace("\n", ""))).is_integer()
    output = []
    for row in string.splitlines():
        output.append([c for c in row])
        for col_idx in range(len(row)//2):
            output[-1][col_idx], output[-1][-col_idx-1] = row[-col_idx-1], row[col_idx]
        output[-1] = "".join(output[-1])
    return "\n".join(output)

UP = (0, 1)
UP_flip = (0, -1)
DOWN = (0, -1)
DOWN_flip = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
TL = (-1, 1)
BL = (-1, -1)
TR = (1, 1)
BR = (1, -1)


def is_integer_negative_support(string):
    try:
        if string[0] == "-" or string[0] == "+":
            return (string[1:]).isnumeric()
        return string.isnumeric()
    except:
        return False


class DIR:
    def __init__(self, should_flip_up_down):
        self.up = (0, 1) if not should_flip_up_down else (0, -1)
        self.down = (0, -1) if not should_flip_up_down else (0, 1)
        self.right = (1, 0)
        self.left = (-1, 0)
        self.top_left = (-1, 1) if not should_flip_up_down else (-1, -1)
        self.bottom_left = (-1, -1) if not should_flip_up_down else (-1, 1)
        self.top_right = (1, 1) if not should_flip_up_down else (1, -1)
        self.bottom_right = (1, -1) if not should_flip_up_down else (1, 1)

    def apply_transformation(self, relative_to, transformation):
        """Transforms the given direction in relative_to by the transformation direction.
        Be aware that diagonal relative_to directions transformed by a diagonal transformation might be wrong.

        Args:
            relative_to (tuple): The direction you want to transform relative to
            transformation (tuple): The transformation direction to be applied

        Returns:
            tuple: The transformed direction
        """
        match transformation:
            case self.up:
                return relative_to
            case self.down:
                match relative_to:
                    case self.up:
                        return self.down
                    case self.down:
                        return self.up
                    case self.left:
                        return self.right
                    case self.right:
                        return self.left
                    case self.top_left:
                        return self.bottom_right
                    case self.top_right:
                        return self.bottom_left
                    case self.bottom_left:
                        return self.top_right
                    case self.bottom_right:
                        return self.top_left
            case self.left:
                match relative_to:
                    case self.up:
                        return self.left
                    case self.down:
                        return self.right
                    case self.left:
                        return self.down
                    case self.right:
                        return self.up
                    case self.top_left:
                        return self.bottom_left
                    case self.top_right:
                        return self.top_left
                    case self.bottom_left:
                        return self.bottom_right
                    case self.bottom_right:
                        return self.top_right
            case self.right:
                match relative_to:
                    case self.up:
                        return self.right
                    case self.down:
                        return self.left
                    case self.left:
                        return self.up
                    case self.right:
                        return self.down
                    case self.top_left:
                        return self.top_right
                    case self.top_right:
                        return self.bottom_right
                    case self.bottom_left:
                        return self.top_left
                    case self.bottom_right:
                        return self.bottom_left
            case self.top_left:
                match relative_to:
                    case self.up:
                        return self.top_left
                    case self.down:
                        return self.bottom_right
                    case self.left:
                        return self.bottom_left
                    case self.right:
                        return self.top_right
                    case self.top_left:
                        return self.left
                    case self.top_right:
                        return self.up
                    case self.bottom_left:
                        return self.down
                    case self.bottom_right:
                        return self.right
            case self.top_right:
                match relative_to:
                    case self.up:
                        return self.top_right
                    case self.down:
                        return self.bottom_left
                    case self.left:
                        return self.top_left
                    case self.right:
                        return self.bottom_right
                    case self.top_left:
                        return self.up
                    case self.top_right:
                        return self.right
                    case self.bottom_left:
                        return self.left
                    case self.bottom_right:
                        return self.down
            case self.bottom_left:
                match relative_to:
                    case self.up:
                        return self.bottom_left
                    case self.down:
                        return self.top_right
                    case self.left:
                        return self.bottom_right
                    case self.right:
                        return self.top_left
                    case self.top_left:
                        return self.right
                    case self.top_right:
                        return self.down
                    case self.bottom_left:
                        return self.up
                    case self.bottom_right:
                        return self.left
            case self.bottom_right:
                match relative_to:
                    case self.up:
                        return self.bottom_right
                    case self.down:
                        return self.top_left
                    case self.left:
                        return self.top_right
                    case self.right:
                        return self.bottom_left
                    case self.top_left:
                        return self.down
                    case self.top_right:
                        return self.left
                    case self.bottom_left:
                        return self.right
                    case self.bottom_right:
                        return self.up


transform = DIR(False).apply_transformation
transform_flip = DIR(True).apply_transformation


def throw():
    raise Exception("Unreachable code detected")


def get_md5_hash(s: str):
    return md5(s.encode()).hexdigest()
