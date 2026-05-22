from math import sqrt, ceil

puzzle_input = 2900000

for num in range(600000, puzzle_input):
    presents = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            presents += divisor
        if presents > puzzle_input:
            print(num)
            break
    # print(num, presents)
# Implement some sort of sieve here
