from helper import input_data, test_data

"""
0 1 10 99 999
    The first stone, 0, becomes a stone marked 1.
    The second stone, 1, is multiplied by 2024 to become 2024.
    The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
    The fourth stone, 99, is split into two stones marked 9.
    The fifth stone, 999, is replaced by a stone marked 2021976.
    
    
    initial:
    0 => 1
    
    even:
    len(str(num))%2 == 0 => split string in half and remove leading zeroes
    
    odd:
    num => num*2024

"""

data = input_data

data = list(map(int, data.strip().split()))

def rules(num):
    retval = []
    num = str(num)
    if num == "0":
        retval.append(1) 
    elif len(num)%2 == 0:
        chars = [a for a in num]
        retval.append(int("".join(chars[: len(chars) // 2])))
        retval.append(int("".join(chars[len(chars) // 2 :])))
    else:
        retval.append(int(num)*2024)
    return retval

for i in range(75):
    fresh = []
    for num in data:    
        fresh.extend(rules(num))
        data = fresh
    print(i)
print(len(data))
