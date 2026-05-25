from helper import problem_data
from collections import defaultdict

bots = defaultdict(list)
outputs = defaultdict(list)
transfers = []
for line in [x.split() for x in problem_data.splitlines()]:
    if line[0] == "value":
        bots[int(line[-1])].append(int(line[1]))
    else:
        transfers.append((int(line[1]), int(line[6]), int(line[-1]), line[5] == "bot", line[-2] == "bot"))
while len(transfers) > 0:
    transfer = transfers.pop(0)
    (bot, low, high, low_is_bot, high_is_bot) = transfer
    if len(bots[bot]) != 2:
        transfers.append(transfer)
        continue
    chips = sorted(bots[bot])
    obj = bots if low_is_bot else outputs
    obj[low].append(chips[0])
    obj = bots if high_is_bot else outputs
    obj[high].append(chips[1])
    if chips == [17, 61]:
        part_1_solution = bot
        print(f"Part 1: {part_1_solution}")

part_2_solution = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(f"Part 2: {part_2_solution}")

assert part_1_solution == 181
assert part_2_solution == 12567
