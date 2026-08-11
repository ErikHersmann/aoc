from helper import problem_data


# problem_data = [int(item.strip()) for item in problem_data.split()]

step = 0

def perform_step(l: list):
    max_ptr = 0
    for idx in range(len(l)):
        if l[idx] > l[max_ptr]:
            max_ptr = idx
    val = l[max_ptr]
    l[max_ptr] = 0
    ptr = max_ptr
    while val > 0:
        ptr = (ptr+1)%len(l)
        l[ptr] += 1
        val -= 1
    return l


seen = {}
output = problem_data
while output not in seen:
    seen[output] = step
    output = "\t".join([str(x) for x in perform_step([int(y) for y in output.split()])])
    step += 1
print(step)
print(step-seen[output])