from helper import problem_data

x_dir = 0 
y_dir = 0 
left = {"N": "W", "W": "S", "S": "E", "E": "N"}
right = {"N": "E", "E": "S", "S": "W", "W": "N"}
current_direction = "N"

visited = set()
found = False
for instruction in problem_data.split(", "):
    direction = instruction[0]
    number = int(instruction[1:])
    current_direction = left[current_direction] if direction == "L" else right[current_direction]
    x_inc, y_inc = 0, 0
    match current_direction:
        case "N":
            y_inc = 1
        case "E":
            x_inc = 1
        case "W":
            x_inc = -1
        case "S":
            y_inc = -1
    for i in range(number):
        x_dir += x_inc
        y_dir += y_inc
        pos = (x_dir, y_dir)
        if not found and pos in visited:
            print(f"Part 2: {abs(x_dir) + abs(y_dir)}")
            found = True
        visited.add(pos)
    
print(f"Part 1: {abs(x_dir) + abs(y_dir)}")
