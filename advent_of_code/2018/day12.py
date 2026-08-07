from helper import problem_data
from copy import deepcopy
from time import sleep

state = "#...#..###.#.###.####.####.#..#.##..#..##..#.....#.#.#.##.#...###.#..##..#.##..###..#..##.#..##..."

transformations = {
    x[0]: x[1] for x in [y.split(" => ") for y in problem_data.splitlines()]
}
generation = 0
min_idx = 0
max_idx = len(state) - 1
state = {idx: c for idx, c in enumerate(state)}
scores = []
max_gen = 100
while generation < max_gen:
    new_state = {}
    min_idx -= 3
    max_idx += 3
    score = 0
    for ptr in range(min_idx, max_idx):
        key = "".join(
            [
                state[index] if (index := ptr + offset) in state else "."
                for offset in range(-2, 3)
            ]
        )
        if key in transformations and transformations[key] == "#":
            new_state[ptr] = "#"
            score += ptr
    state = deepcopy(new_state)
    generation += 1
    scores.append(score)
# Check for when GOL stabilizes, after this the indices get offset by 22 every generation (taking 100 as absolute here we calculate the remaining iterations to target and multiply by the score difference for a single iteration. Finally we add the score we had at 100 already.)
print((scores[-1]-scores[-2]) * (50000000000 - max_gen) + scores[-1])
