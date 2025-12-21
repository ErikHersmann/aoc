from collections import defaultdict
from helper import input_data, test_data

data = test_data

data = [[a for a in b] for b in data.splitlines()]
h, w = len(data), len(data[0])
UP, DOWN, RIGHT, LEFT = (-1, 0), (1, 0), (0, 1), (0, -1)
DIRS = [UP, DOWN, RIGHT, LEFT]

# Return sum of area*perimeter of all fenced in areas
def oob(pos):
    (x, y) = pos
    return x < 0 or y < 0 or x > h-1 or y > w-1

# Check in all 4 directions and recurse until either oob, not the right char, or in visited
# Visited should be a set and also have a dictionary of neighborcount for each
# once the entire recursion is finished we return (4 * visited - sum(neighborcount))*visited
# and we extend the banned nodes by the visited so further recursions don't use those

def get_side_count(nodes):
    # Just detect the number of fused edges and return that and subtract it from the perimeter
    rows = defaultdict(list)
    cols = defaultdict(list)
    for (row, col) in nodes:
        rows[row].append(col)
        cols[col].append(row)
    print(rows)
    print(cols)
    # For each row
    # Go through the cols (if diff is bigger than 1 in the sorted that is an extra 4 sides, else 1) so 1 + number of bigger diffs * 4
    return 1

def compute_score(r, c):
    nodes = set()
    nodes.add((r, c))
    neighbors = defaultdict(int)
    # Extend nodes until all recursion paths are exhausted
    def search(r, c):
        valid_neighbors = []
        for dir in DIRS:
            neighbor = (r+dir[0], c+dir[1])
            # Parse out all incorrect type neighbors
            # Parse out all already visited neighbors
            # Parse out all oob neighbors
            if (
                not oob(neighbor)
                and data[neighbor[0]][neighbor[1]] == data[r][c]
            ):
                neighbors[(r, c)] += 1
                if neighbor not in nodes:
                    valid_neighbors.append(neighbor)

        # Recurse all neighbors (these have not been visited)
        nodes.update(valid_neighbors)
        for pos in valid_neighbors:
            search(pos[0], pos[1])
    search(r, c)
    # Return (points, visited)
    # Get perimeter from nodes
    sides = get_side_count(nodes)
    perimeter = 4 * len(nodes) - sum([value for _, value in neighbors.items()])
    area = len(nodes)
    score1 = perimeter * area
    score2 = area * sides
    return (score1, nodes, score2)


total1 = 0
total2 = 0
visited = set()
for r in range(h):
    for c in range(w):
        if (r, c) not in visited:
            (points1, nodes, points2) = compute_score(r, c)
            total1 += points1
            total2 += points2
            visited.update(nodes)

print(total1)
print(total2)
