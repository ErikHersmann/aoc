from helper import input_data


def part_1(available: list, fresh: list):
    fresh_available = set()
    for ingredient in available:
        for start, end in fresh:
            if start <= ingredient <= end:
                fresh_available.add(ingredient)
                break
    print(len(fresh_available))
    return len(fresh_available)

def part_2(fresh:list):
    res = 0
    has_merged  = True
    while has_merged:
        has_merged = False
        n = len(fresh)
        merged = {}
        to_be_removed_indices = set()
        for idx1 in range(n):
            for idx2 in range(n):
                if idx1 == idx2: continue
                (start_1, end_1) = fresh[idx1]
                (start_2, end_2) = fresh[idx2]
                assert not(start_1 == start_2 and end_1 == end_2)
                assert start_1 <= end_1
                assert start_2 <= end_2
                if start_1 <= start_2 and end_1 >= end_2:
                    to_be_removed_indices.add(idx2)
                    has_merged = True
                elif start_2 <= start_1 and end_2 >= end_1:
                    to_be_removed_indices.add(idx1)
                    has_merged = True
                elif end_1 >= start_2 and start_1 <= start_2:
                    to_be_removed_indices.add(idx1)
                    to_be_removed_indices.add(idx2)
                    merged[start_1] = end_2
                    has_merged = True
                elif end_2 >= start_1 and start_2 <= start_1:
                    to_be_removed_indices.add(idx1)
                    to_be_removed_indices.add(idx2)
                    merged[start_2] = end_1
                    has_merged = True
        for idx in sorted(list(to_be_removed_indices), reverse=True):
            fresh.pop(idx)
        for start, end in merged.items():
            new_item = [start, end]
            if new_item not in fresh:
                fresh.append([start, end])
    for start, end in fresh:
        res += end-start + 1
    print(res)
    return res


data = input_data

fresh, available = [x.splitlines() for x in data.split("\n\n")]
fresh = list(set(fresh))
available = [int(x) for x in available]
fresh = [[int(x[0]), int(x[1])] for x in [y.split("-") for y in fresh]]
part_1(available=available, fresh=fresh)
fresh = sorted(fresh, key=lambda x: x[1])
part_2(fresh)
