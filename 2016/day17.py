from helper import problem_data, get_md5_hash, throw, maxsize


problem_data = "edjrjqaa"
width, height = 4, 4
start = (0, 0)
target = (3, 3)
opens = "b,c,d,e,f".split(",")
best = [maxsize]
worst = [0]

def dp(path: str, pos: tuple):
    global best, worst
    if pos == target:
        if len(path) < best[0]:
            best = [len(path), path]
        if len(path) > worst[0]:
            worst = [len(path), path]
        return
    (row, col) = pos
    up, down, left, right = [x in opens for x in get_md5_hash(problem_data + path)[:4]]
    if up and row > 0:
        dp(path + "U", (row - 1, col))
    if down and row < height - 1:
        dp(path + "D", (row + 1, col))
    if left and col > 0:
        dp(path + "L", (row, col - 1))
    if right and col < width - 1:
        dp(path + "R", (row, col + 1))

dp("", start)
print(f"Part 1: {best[1]}")
print(f"Part 2: {worst[0]}")