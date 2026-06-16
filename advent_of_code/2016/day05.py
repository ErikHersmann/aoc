from hashlib import md5
problem_data = "reyedfim"

password = ["" for _ in range(8)]
i = 0
while True:
    i += 1
    hash_val = md5(f"{problem_data}{i}".encode()).hexdigest()
    if hash_val.startswith("00000"):
        if hash_val[5] in [str(x) for x in range(8)]:
            password[int(hash_val[5])] = hash_val[6] if password[int(hash_val[5])] == "" else password[int(hash_val[5])]
            print(password)
            if "" not in password:
                break
