from helper import problem_data

total = 0
for line in problem_data.splitlines():
    name, checksum = line.replace("[", " ").rstrip("]").split()
    checksum = [c for c in checksum]
    checksum_nums= None
    sector_id = name.split("-")[-1]
    name = [c for c in name.replace(sector_id, "") if c != "-"]
    sector_id = int(sector_id)
    invalid = False
    for idx, c in enumerate(checksum):
        counter = name.count(c)
        if not checksum_nums:
            checksum_nums = [counter]
        else:
            if checksum_nums[-1] < counter:
                invalid = True
            elif checksum_nums[-1] == counter and ord(c) < ord(checksum[idx-1]):
                invalid = True
            checksum_nums.append(counter)
    total += sector_id if not invalid else 0
print(total)