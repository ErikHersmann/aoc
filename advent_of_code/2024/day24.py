from helper import test_data, test_data_2, input_data

data = input_data

data = data.split("\n\n")

registers, gates = map(lambda x: x.splitlines(), data)

registers = {key: int(value) for (key, value) in map(lambda y: y.split(": "), registers)}
operations = []
for op in gates:
    first, second = op.split(" -> ")
    operations.append((*first.split(), second))
gates = operations

iterations = 0
while True:
    one_pass_fail = False
    iterations += 1
    for gate in gates:
        (input1, operation, input2, output) = gate
        if input1 not in registers or input2 not in registers: 
            one_pass_fail = True
            continue
        match operation:
            case "AND":
                registers[output] = registers[input1] and registers[input2]
            case "OR":
                registers[output] = registers[input1] or registers[input2]
            case "XOR":
                registers[output] = registers[input1] ^ registers[input2]
    if not one_pass_fail: 
        break

res = []
z_keys = sorted([key for key in registers.keys() if "z" == key[0]])
for power, key in enumerate(z_keys):
    res.append(registers[key])
decimal_result = int("".join([str(x) for x in res[::-1]]), 2)
print(decimal_result)
