from helper import problem_data, test_data, example_data

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
# but not like aaa (aa, but it overlaps).

# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

BANNED = set("ab,cd,pq,xy".split(","))
VOWELS = set([a for a in "aeiou"])

def part_1(string: str):
    # 3
    for ban in BANNED:
        if ban in string:
            return 0
    # 2
    vowel_count = int(string[0] in VOWELS)
    consecutive = False
    for idx in range(len(string)-1):
        if string[idx] == string[idx+1]:
            consecutive = True
        if string[idx+1] in VOWELS:
            vowel_count += 1
    return int(vowel_count >= 3 and consecutive)


def part_2(string: str):
    # 1
    multipair = False
    for idx in range(len(string) - 1):
        if string.count(string[idx] + string[idx + 1]) >= 2:
            multipair = True
    # 2
    sandwich = False
    for idx in range(1, len(string) - 1):
        if string[idx-1] == string[idx + 1]:
            sandwich = True
            break
    return int(sandwich and multipair)


def is_nice(is_part_one: bool, string: str):
    if is_part_one:
        return part_1(string)
    return part_2(string)

res1 = 0
res2 = 0
for s in problem_data.splitlines():
    if is_nice(True, s):
        res1 += 1
    if is_nice(False, s):
        res2 += 1

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")
