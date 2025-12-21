from collections import defaultdict
from helper import input_data, test_data, test_data_2
from sys import argv
from colorama import Fore, Back


# 1..1000 | ForEach-Object { Write-Host "Running iteration $_" -ForegroundColor Yellow; python day14.py $_ ; Start-Sleep 0.6 }
# h, w = 7, 11
h, w = 103, 101
my, mx = h//2, w//2

data = input_data


data = [line.replace("p=", "").split(" v=") for line in data.splitlines()]
i_positions = []
i_velocities = []
p_positions = []
for line in data:
    i_positions.append(tuple(map(int, line[0].split(","))))
    i_velocities.append(tuple(map(int, line[1].split(","))))

def is_oob(pos):
    (x, y) = pos
    return x == mx or y == my

def mapped(pos, velocity, seconds):
    (x, y) = pos
    (v1, v2) = velocity
    p_x = x
    p_y = y
    for i in range(1, seconds):
        p_x += v1
        p_x %= w
        if p_x == x:
            break
    for _ in range(0, seconds%i):
        p_x += v1
        p_x %= w
    for i in range(1, seconds):
        p_y += v2
        p_y %= h
        if p_y == y:
            break
    for _ in range(0, seconds % i):
        p_y += v2
        p_y %= h
    # Simulate until we hit the start again (mode the total move count by that number and then simulate the remainder)
    # worry about x and y individually since they don't influence one another?
    return (p_x, p_y)

def get_quadrant(pos):
    # return 0 to 3
    (x, y) = pos
    if x < mx and y < my:
        return 0
    if x > mx and y < my:
        return 1
    if x > mx and y > my:
        return 2
    if x < mx and y > my:
        return 3
    return -1
def calculate_score_1(positions):
    scores = [0,0,0,0]
    for pos in positions:
        if is_oob(pos): continue
        idx = get_quadrant(pos)

        if idx > -1:
            scores[idx] += 1
    res = 1
    for val in scores:
        if val != 0:
            res *= val
    return res

def pprint(interval, positions):
    print(Fore.WHITE + f"{interval}")
    for y in range(h):
        for x in range(w):
            if (x, y) in positions:
                print(Fore.GREEN + Back.GREEN + "#", end="")
            else:
                print(Fore.BLACK + Back.BLACK +".", end="")
        print(Back.BLACK)

upper_bound = int(argv[1] if len(argv) == 2 else 10000)
candidates = set()
iterator = list(zip(i_positions, i_velocities))
for seconds in range(2, upper_bound):
    rowwise = defaultdict(int)
    p_positions = set()
    for pos, vel in iterator:
        p_pos = mapped(pos, vel, seconds)
        rowwise[p_pos[0]] += 1
        if rowwise[p_pos[0]] > 30: 
            candidates.add(seconds)
        p_positions.add(p_pos)
    if seconds == 100:
        part1 = calculate_score_1(p_positions)
    if seconds in candidates:
        pprint(seconds, p_positions)
print(Fore.WHITE + Back.BLACK+ f"part 1 solution {part1}")
print(candidates)