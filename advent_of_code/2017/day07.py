from helper import problem_data
from collections import deque, defaultdict

unvisited = deque(problem_data.splitlines())
data = problem_data.splitlines()


def parent_transform(parent: str):
    name, weight = parent.split()
    return name, int(weight[1:-1])


d_flat = defaultdict(list)
gkids = set()
while len(unvisited) > 1:
    current_node = unvisited.popleft()
    if "->" not in current_node:
        continue
    parent, kids = current_node.split(" -> ")
    pname, pweight = parent_transform(parent)
    kids = kids.split(", ")
    d_flat[pname] = (pweight, kids)
    for kid in kids:
        gkids.add(kid)
    if pname not in gkids:
        unvisited.append(current_node)
print(f"Part 1: {unvisited.pop().split("(")[0].strip()}")


leaf_nodes = {}
non_leaf_nodes = deque()
for line in data:
    if "->" not in line:
        n,w = parent_transform(line)
        assert n not in leaf_nodes
        leaf_nodes[n] = w
    else:
        parent, kids = line.split(" -> ")
        name, weight = parent_transform(parent)
        non_leaf_nodes.append((name, weight, kids.split(", ")))

while len(non_leaf_nodes) > 0:
    cur_non_leaf = non_leaf_nodes.popleft()
    if all([kid in leaf_nodes for kid in cur_non_leaf[2]]):
        temp = []
        for kid in cur_non_leaf[2]:
            temp.append(leaf_nodes.pop(kid))
        if len(set(temp)) != 1: print(f"Problematic weight is in here: {temp}, needed abs diff: {max(temp)-min(temp)}")
        weight = cur_non_leaf[1]+sum(temp)
        if weight == 1579: # set this to the problematic weight from above
            print(f"Part 2-ish: {cur_non_leaf[1]}-absolute diff should be the solution")
            pass
        leaf_nodes[cur_non_leaf[0]] = weight
    else:
        non_leaf_nodes.append(cur_non_leaf)

# 1513 + 33 + 33 = 1579