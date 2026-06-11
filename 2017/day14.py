problem_data = "oundnydw"

for i in range(128):
    hash_ = f"{problem_data}-{i}"
    for c in hash_:
        bin(int(c, base=16))
