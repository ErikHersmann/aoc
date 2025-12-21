from collections import defaultdict
from doctest import debug
from enum import Enum
from xmlrpc.client import MAXINT

from sympy import true


with open("input.txt", "r") as f:
    input_data = f.read()

with open("test.txt", "r") as f:
    test_data = f.read()

with open("test2.txt", "r") as f:
    test_data_2 = f.read()


class Dijkstra:
    def __init__(
        self,
        unvisited: set,
        start: tuple,
        target: tuple,
        height: int,
        width: int,
        map: list,
    ):
        """
        Positions and directions are always a tuple of (x, y), whereas the map is indexed as [y][x]
        """
        self.NORTH = (0, -1)
        self.SOUTH = (0, 1)
        self.EAST = (1, 0)
        self.WEST = (-1, 0)
        self.LEFT = {
            self.EAST: self.NORTH,
            self.NORTH: self.WEST,
            self.WEST: self.SOUTH,
            self.SOUTH: self.EAST,
        }
        self.RIGHT = {
            self.EAST: self.SOUTH,
            self.NORTH: self.EAST,
            self.WEST: self.NORTH,
            self.SOUTH: self.WEST,
        }
        self.unvisited = unvisited
        self.start = start
        self.target = target
        self.visited = set()
        # Dict of pos: set of tuples of (pos, dir)
        self.predecessors = defaultdict(lambda: set())
        # Dict of pos: cost
        self.shortest_dist = defaultdict(lambda: MAXINT)
        self.HEIGHT = height
        self.WIDTH = width
        self.map = map
        self.WALL_CHAR = "#"

    def __get_cheapest_unvisited(self):
        closest = [None, MAXINT]
        for node in self.unvisited:
            if self.shortest_dist[node] <= closest[1]:
                closest = [node, self.shortest_dist[node]]
        closest = closest[0]
        dirs = set()
        for predecessor in self.predecessors[closest]:
            dirs.add(predecessor.dir)
        return (closest, dirs)

    class __direction(Enum):
        FORWARD = (0,)
        RIGHT = (1,)
        LEFT = 2

    class __predecessor:
        def __init__(self, pos, dir):
            self.pos = pos
            self.dir = dir

    def __out_of_bounds(self, pos, dir):
        (x, y) = self.__add_position_and_direction(pos, dir)
        return self.map[y][x] == self.WALL_CHAR

    def __add_position_and_direction(self, pos, dir):
        (dx, dy) = dir
        (px, py) = pos
        return (dx + px, dy + py)

    def __get_neighbor(self, pos, dir, direction):
        cost = 1001
        match direction:
            case self.__direction.LEFT:
                dir = self.LEFT[dir]
            case self.__direction.RIGHT:
                dir = self.RIGHT[dir]
            case self.__direction.FORWARD:
                cost = 1
        return (
            self.__predecessor(self.__add_position_and_direction(pos, dir), dir),
            self.shortest_dist[pos] + cost,
        )

    def __get_neighbors_with_cost(self, pos, dir):
        """_summary_

        Args:
            pos (_type_): _description_

        Returns:
            list: List of tuples of form (pos, cost)
        """
        forward_neighbor = self.__get_neighbor(pos, dir, self.__direction.FORWARD)
        left_neighbor = self.__get_neighbor(pos, dir, self.__direction.LEFT)
        right_neighbor = self.__get_neighbor(pos, dir, self.__direction.RIGHT)
        return [
            neighbor
            for neighbor in [forward_neighbor, left_neighbor, right_neighbor]
            if neighbor
        ]

    def __print_shortest(self, debug: bool):
        self.__debug = []
        for row in range(self.HEIGHT):
            self.__debug.append([])
            for col in range(self.WIDTH):
                key = (col, row)
                self.__debug[-1].append(
                    f"{self.shortest_dist[key]:<5}"
                    if self.shortest_dist[key] < MAXINT
                    else f"{'#####':<5}"
                )
        if debug:
            print("\n".join([" ".join(a) for a in self._Dijkstra__debug]))

    def solve_part_1(self):
        """solves the first part

        Returns:
            int: returns the shortest distance to the target node from the start node
        """
        current = self.start
        self.shortest_dist[current] = 0
        self.predecessors[current].add(self.__predecessor(None, self.EAST))
        while len(self.unvisited) > 0:
            (current, dirs) = self.__get_cheapest_unvisited()
            self.unvisited.remove(current)
            for start_dir in dirs:
                neighbors = self.__get_neighbors_with_cost(current, start_dir)
                # Update all neighbors
                for node, cost in neighbors:
                    # Cheaper update and remove old
                    if self.shortest_dist[node.pos] > cost:
                        self.shortest_dist[node.pos] = cost
                        self.predecessors[node.pos] = set()
                        self.predecessors[node.pos].add(self.__predecessor(current, node.dir))
                    # Same cost: add to alternatives
                    elif self.shortest_dist[node.pos] == cost:
                        self.predecessors[node.pos].add(self.__predecessor(current, node.dir))
        self.__print_shortest(true)
        return self.shortest_dist[self.target]

    def solve_part_2(self):
        """solves the second part

        Returns:
            int: length of nodes that are on one of the optimal paths
        """
        self.optimal_paths_members = set()
        self.__walk_backwards(self.target)
        return len(self.optimal_paths_members)

    def __walk_backwards(self, current):
        if current == self.start:
            return
        self.optimal_paths_members.add(current)
        # If empty this just returns the recursion
        for node, _ in self.predecessors[current]:
            self.solve_part_2(node)
