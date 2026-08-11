from helper import problem_data
from collections import deque, defaultdict

l = deque(problem_data.splitlines())


def parent_transform(parent: str):
    name, weight = parent.split()
    return name, int(weight[1:-1])


d_flat = defaultdict(list)
gkids = set()
while len(l) > 1:
    cur = l.popleft()
    if "->" not in cur:
        continue
    parent, kids = cur.split(" -> ")
    pname, pweight = parent_transform(parent)
    kids = kids.split(", ")
    dflat[pname] = (pweight, kids)
    for kid in kids:
        gkids.add(kid)
    if pname not in gkids:
        l.append(cur)
print(l)

# Since we found out the root node from step 1 we can construct the graph in order now
# After that we run dfs with bfs ? wtfuckery

# d_complex = {}

# q = deque(["hlhomy"])
# while len(q) > 0:
#     cached_len = len(q)
#     for _ in range(cached_len):
#         cur = q.popleft()


# For that we need a dictionary, I'm about to lose it
def dfs(node, running_sum):
    if 


# Can't wrap my head around this
# maybe this is just dfs 


# Push values back onto a stack and if the values dont' match top of stack we are either one level up or it's wrong 