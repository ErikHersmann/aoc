from helper import input_data, test_data, test_data_2, Dijkstra


data = test_data

data = [[a for a in b] for b in data.splitlines()]

height = len(data)
width = len(data[0])
unvisited = set()
for row in range(height):
    for col in range(width):
        pos = (col, row)
        match data[row][col]:
            case "#":
                continue
            case "E":
                target = pos
                unvisited.add(pos)
            case "S":
                start = pos
                unvisited.add(pos)
            case ".":
                unvisited.add(pos)

dijkstra = Dijkstra(unvisited=unvisited, start=start, target=target, height=height, width=width, map=data)

print(dijkstra.solve_part_1())
# print(dijkstra.solve_part_2())

# 82484 too high
# 82484 incorrect
# 81483 too low
# 81484 incorrect
