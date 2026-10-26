from helper import problem_data

data = list(map(int, problem_data.split(",")))

# data = [3,4,3,1,2]

max_timer = 8
ages = [0 for _ in range(max_timer+1)]
for fish in data:
    ages[fish] += 1

part_1 = True
for day in range(1, (81 if part_1 else 257)):
    temp = [0 for _ in range(max_timer+1)]
    temp[max_timer] += ages[0]
    temp[max_timer-2] += ages[0]
    for idx in range(max_timer):
        temp[idx] += ages[idx+1]
    ages = temp
print(day, sum(ages))