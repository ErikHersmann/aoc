from hashlib import md5

problem_data = "yzbqklnj"
number = 0
results = []
while True:
    hash_value = md5((problem_data+str(number)).encode()).hexdigest()
    if len(results) == 0 and hash_value.startswith("0"*5):
        results.append(number)
    if hash_value.startswith("0"*6):
        results.append(number)
        break
    number += 1
print("\n".join([f"Part {i+1}: {results[i]}" for i in range(2)]))