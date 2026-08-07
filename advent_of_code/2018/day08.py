from helper import problem_data
from collections import deque, defaultdict

stack = deque()
stack.append((True, 1, 0))
part_1_sum = 0

problem_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

node_id = 0
valid_ids = set()
cache = defaultdict(list)
data = [int(x) for x in problem_data.split()]
idx = 0
while idx < len(data):
    metadata_count, node_count, number = 0, 0, 0
    (should_read_nodes, number, n_id) = stack.pop()
    if should_read_nodes:
        number -= 1
        if number > 0:
            stack.append((True, number, n_id))
        node_count = data[idx]
        idx += 1
        metadata_count = data[idx]
        if metadata_count > 0:
            stack.append((False, metadata_count, node_id))
        if node_count > 0:
            stack.append((True, node_count, node_id))
        else:
            valid_ids.add(node_id)
        idx += 1
        # print(f"{chr(node_idx)}\t{node_count}\t{metadata_count}")
        node_id += 1
    else:
        # print(f"{chr(node_idx)}" ,end=": ")
        temp = 0
        while number > 0:
            # print(data[idx] ,end=", ")
            part_1_sum += data[idx]
            temp += data[idx]
            idx += 1
            number -= 1
        cache[n_id].append(temp)
        # print()
        # Read metadata
print(part_1_sum)