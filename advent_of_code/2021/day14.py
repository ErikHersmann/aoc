from helper import problem_data, throw
from collections import defaultdict
from copy import deepcopy



template, transitions = problem_data.split("\n\n")
transition_dict = {}

for transition in transitions.splitlines():
    base, insertion = transition.split(" -> ")
    if base in transition_dict:
        throw()
    transition_dict[base] = insertion
pass

char_counter_dict = defaultdict(int)
template_dict = defaultdict(int)
for i in range(len(template)-1):
    key = "".join(template[i:i+2])
    template_dict[key] += 1
        

counts = defaultdict(int)
template = [c for c in template]
for c in template:
    counts[c] += 1
    char_counter_dict[c] += 1
number_of_steps = 10
for step in range(1, number_of_steps + 1):
    i = 0
    while i < len(template):
        key = ''.join(template[i:i+2])
        if key in transition_dict:
            new_element = transition_dict[key]
            template.insert(i+1, new_element)
            counts[new_element] += 1
            i += 1
        i += 1

res = sorted(counts.values())

print(f"Part 1: {res[-1] - res[0]}")

# The input should just be a dictionary of pairs and their counts in the input
# Each transition simply removes 1 from the current pair and adds +1 for the 2 new pairs

new_dict = {}
for key, value in transition_dict.items():
    new_dict[key] = [key[0] + value, value + key[1]]

for step in range(1, 41):
    new_template_dict = defaultdict(int)
    for pair, count in template_dict.items():
        if len(new_dict[pair]) < 1:
            throw()
        for new_pair in new_dict[pair]:
            new_template_dict[new_pair] += count
        char_counter_dict[transition_dict[pair]] += count
    template_dict = new_template_dict

final_dict = defaultdict(int)
for pair, count in template_dict.items():
    for c in pair:
        final_dict[c] += count

res = sorted([val for _, val in char_counter_dict.items()])
print(f"Part 2: {res[-1]-res[0]}")

# Clean up this clusterfuck