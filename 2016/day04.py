from helper import problem_data
from collections import defaultdict


def decrypt(s, sector_id):
    return "".join(
        [
            chr(((ord(c) - ord("a") + sector_id) % 26) + ord("a")) if c != "-" else " "
            for c in s
        ]
    )


def get_five_most_common_chars(s):
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    a = sorted(
        [(count, c) for c, count in counts.items() if c.isalpha()],
        reverse=True,
        key=lambda x: (x[0], -ord(x[1])),
    )[:5]
    return "".join([x[1] for x in a])


def get_sector_id(line):
    right_side = line.split("-")[-1].rstrip("]").split("[")
    sector_id = right_side[0]
    left_side = line.split(sector_id)[0].rstrip("-")
    decrypted = decrypt(left_side, int(sector_id))
    if "north" in decrypted:
        print(decrypted, sector_id)
    return (
        0 if get_five_most_common_chars(left_side) != right_side[1] else int(sector_id)
    )


print(sum([get_sector_id(line) for line in problem_data.splitlines()]))
