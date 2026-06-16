from helper import input_data
from math import dist, prod

data = input_data
data = [[int(y) for y in x.split(",")] for x in data.splitlines()]

n = len(data)
distances = sorted(
    [
        [dist(data[idx1], data[idx2]), idx1, idx2]
        for idx2 in range(n)
        for idx1 in range(n)
        if idx1 > idx2
    ],
    key=lambda x: x[0],
)

sets = []
member_map = {}
longest_set = 0
for _, index_1, index_2 in distances:
    if index_1 == distances[999][1] and index_2 == distances[999][2]:
        set_sizes = sorted([len(set) for set in sets], reverse=True)
        print(f"Part 1: {prod(set_sizes[:3])}")
    if index_1 in member_map:
        if index_2 in member_map and member_map[index_1] != member_map[index_2]:
            old_set_idx = member_map[index_2]
            for vis in sets[member_map[index_2]]:
                sets[member_map[index_1]].add(vis)
                member_map[vis] = member_map[index_1]
            sets[old_set_idx] = set()
            longest_set = max(longest_set, len(sets[member_map[index_1]]))
        else:
            sets[member_map[index_1]].add(index_2)
            member_map[index_2] = member_map[index_1]
            longest_set = max(longest_set, len(sets[member_map[index_1]]))
    else:
        if index_2 in member_map:
            sets[member_map[index_2]].add(index_1)
            member_map[index_1] = member_map[index_2]
            longest_set = max(longest_set, len(sets[member_map[index_2]]))
        else:
            sets.append(set([index_1, index_2]))
            member_map[index_1] = len(sets) - 1
            member_map[index_2] = len(sets) - 1
    if longest_set == 1000:
        print(f"Part 2: {data[index_1][0] * data[index_2][0]}")
        break
