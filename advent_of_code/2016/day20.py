from helper import problem_data

ranges = sorted(
    [tuple(map(int, line.split("-"))) for line in problem_data.splitlines()],
    key=lambda x: x[0],
)

idx = 0
while len(ranges) > 1 and idx < len(ranges) - 1:
    # It's only  efficient to pre pop if we have more merging than skipping I think
    (s1, e1), (s2, e2) = ranges.pop(idx), ranges.pop(idx)
    if s2 - e1 <= 1:
        ranges.insert(idx, (s1, max(e1, e2)))
        continue
    ranges.insert(idx, (s2, e2))
    ranges.insert(idx, (s1, e1))
    idx += 1

print(f"Part 1: {ranges[0][1]+1}")
print(
    f"Part 2: {sum([ranges[idx][0]-ranges[idx-1][1] - 1 for idx in range(1, len(ranges))])}"
)
