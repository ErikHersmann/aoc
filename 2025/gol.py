from sys import argv, maxsize, stdout
from time import sleep
import json
from colors import Color
from termcolor import cprint

MAXINT = maxsize
MININT = -maxsize


# All cells are dead by default
class Game:
    def __init__(self, birth_rule=None, death_rule=None) -> None:
        if not birth_rule or not death_rule:
            self.___init___()
        else:
            self._birth_rule = set(list(birth_rule))
            self._death_rule = set(list(death_rule))
        self.live_cells = set()
        self.OFFSETS = [-1, 0, 1]
        self.max_row = MININT
        self.max_col = MININT
        self.min_row = MAXINT
        self.min_col = MAXINT
        self.iteration = 0
        self.ages = {}

    def initialize(self, live_cells: set):
        self.live_cells = self.live_cells.union(live_cells)

    def decide_cell_state(self, neighbor_count: int, cell_state: int) -> int:
        if not cell_state:
            return neighbor_count in self._birth_rule
        else:
            return neighbor_count in self._death_rule

    def ___init___(self):
        if len(argv) == 2:
            notation = argv[1]
        else:
            notation = "B3/S23"
        params = [[int(y) for y in x[1:]] for x in notation.split("/")]
        self._birth_rule, self._death_rule = params

    def update_bounding_area(self, position: tuple):
        (row, col) = position
        self.max_col = max(self.max_col, col)
        self.max_row = max(self.max_row, row)
        self.min_col = min(self.min_col, col)
        self.min_row = min(self.min_row, row)

    def set_ages(self):
        for cell in self.live_cells:
            self.ages[cell] = self.iteration

    def step(self):
        to_be_deleted = set()
        to_be_added = set()
        for cell in self.live_cells:
            self.update_bounding_area(cell)
            neighbors = self.get_neighbors(cell)
            neighbor_count = self.get_live_neighbor_count(cell, neighbors)
            if not self.decide_cell_state(neighbor_count, 1):
                to_be_deleted.add(cell)
            for neighbor in neighbors:
                if neighbor in self.live_cells:
                    continue
                if self.decide_cell_state(
                    self.get_live_neighbor_count(
                        neighbor, self.get_neighbors(neighbor)
                    ),
                    0,
                ):
                    self.update_bounding_area(neighbor)
                    self.ages[neighbor] = self.iteration
                    to_be_added.add(neighbor)
        self.live_cells = self.live_cells.union(to_be_added)
        for rem in to_be_deleted:
            self.live_cells.remove(rem)
        self.iteration += 1
        return

    def get_live_neighbor_count(self, position: tuple, neighbors: set) -> int:
        return sum([neighbor in self.live_cells for neighbor in neighbors])

    def get_neighbors(self, position: tuple):
        neighbors = set()
        (row, col) = position
        for row_offset in self.OFFSETS:
            for col_offset in self.OFFSETS:
                if row_offset == 0 and col_offset == 0:
                    continue
                neighbors.add((row + row_offset, col + col_offset))
        return neighbors

    def visualize(self):
        print("_" * (self.max_col - self.min_col))
        print(f"{self.iteration} ({self.min_row}, {self.min_col})", end="")
        for row in range(self.min_row - 1, self.max_row + 1):
            for col in range(self.min_col - 1, self.max_col + 1):
                pos = (row, col)
                cprint(
                    "#" if pos in self.live_cells else " ",
                    end="",
                    color=(
                        Color[self.ages[pos] % len(Color)]
                        if pos in self.ages
                        else "white"
                    ),
                )
                if row == self.max_row and col == self.max_col:
                    print(f"{self.iteration} ({self.max_row}, {self.max_col})", end="")
            print()

    def add_glider(self, position: tuple):
        """Adds a glider to the specified position (bottom right of the glider)

        Args:
            position (tuple): Specifies the bottom rightmost cell of the glider
        """
        # Maybe allow for rotation in here too
        (row, col) = position
        self.live_cells.add(position)
        self.live_cells.add((row - 1, col))
        self.live_cells.add((row - 2, col - 1))
        self.live_cells.add((row, col - 1))
        self.live_cells.add((row, col - 2))


game = Game()
initial_cells = set()
# 10-11, 18 stagnate
for i in range(14):
    initial_cells.add((i, i))
    initial_cells.add((i, -i))
    initial_cells.add((-i, -i))
    initial_cells.add((-i, i))
    initial_cells.add((4, i))
    initial_cells.add((-5, i))
    initial_cells.add((-7, i))
    initial_cells.add((-9, i))
    initial_cells.add((7, i))
    initial_cells.add((i, 7))
    initial_cells.add((-i, 7))
    initial_cells.add((i, 10))
    initial_cells.add((-i, 10))
game.initialize(initial_cells)
game.add_glider((-12, -12))
game.add_glider((-12, -4))
game.add_glider((-12, -8))
with open("starting_states/starts.txt", "a+") as f:
    json.dump(list(game.live_cells), f)
    f.write("\n")
for _ in range(100000):
    game.step()
    game.visualize()
    sleep(0.25)
