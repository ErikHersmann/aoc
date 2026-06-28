# Issue: idea is there but not working on test case

from hashlib import md5
from collections import defaultdict

# TODO: Doesn't even work on sample input
problem_data = "abc"

# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

pending_threes = defaultdict(list)
pending_fives = defaultdict(list)
valid_one_time_pad_keys = []

for i in range(22729):
    hash_val = md5(f"{problem_data}{i}".encode()).hexdigest()
    idx = 0
    updated = False
    while idx < len(hash_val):
        c = hash_val[idx]
        count = 1
        idx += 1
        while idx < len(hash_val) and hash_val[idx] == c:
            count += 1
            idx += 1
        if count == 3:
            pending_threes[i].append(c)
            break
        elif count >= 5:
            updated = True
            pending_fives[c].append(i)
    if updated:
        for resolver in pending_fives:
            for potential_index, potential_keys in pending_threes.items():
                for potential_key in potential_keys:
                    if resolver == potential_key:
                        for resolver_index in pending_fives[resolver]:
                            if potential_index < resolver_index <= potential_index + 1000:
                                valid_one_time_pad_keys.append((potential_key, potential_index, pending_fives[resolver]))
                                pending_threes[potential_index].remove(resolver)
                                break
    if len(valid_one_time_pad_keys) >= 64:
        print(i)
        break
pass