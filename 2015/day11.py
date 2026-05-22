from helper import problem_data, throw

BANNED = set([ord(x) - 1 for x in ["i", "o", "l"]])
def check(password: list):
    found = False
    pairs = set()
    for idx in range(1, len(password) - 1):
        prev, cur, next = password[idx-1:idx+2]
        if not found and prev + 1 == cur == next-1:
            found = True
        elif cur == next:
            pairs.add(password[idx])
    return len(pairs) >= 2 and found

pw = [ord(x) for x in problem_data]
found_once = False
end, start = ord("z")+1, ord("a")
while True:
    ptr = len(pw)-1
    pw[ptr] += 1
    while pw[ptr] == end:
        pw[ptr] = start
        ptr -= 1
        pw[ptr] += 1 if pw[ptr] not in BANNED else 2
    if check(pw):
        if found_once:
            print("Part 2: " + "".join([chr(x) for x in pw]))
            break
        found_once = True
        print("Part 1: " + "".join([chr(x) for x in pw]))
