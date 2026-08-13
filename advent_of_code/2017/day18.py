from helper import problem_data, is_integer_negative_support
from copy import deepcopy
from collections import defaultdict, deque
from multiprocessing import Pool, Process, Array, freeze_support, Pipe, Lock, Queue
from copy import deepcopy
# problem_data = """snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d"""
instr = problem_data.splitlines()

def run_program(index, registers, instruction_pointer, instructions, receive_q: Queue, send_q: Queue, lock: Lock):
    send_count = 0
    while instruction_pointer < len(instructions):
        if not send_count%10000000:
            if lock.acquire(True):
                print(index, send_count, registers)
                lock.release()
        cur = instructions[instruction_pointer].split()
        match cur[0]:
            case "snd":
                # arg = int(cur[1]) if is_integer_negative_support(cur[1]) else registers[cur[1]]
                # if lock.acquire(True):
                #     print(index, f"Sending: {arg}")
                #     lock.release()
                # send_q.put(arg)
                instruction_pointer += 1
                send_count += 1
            case "set":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                registers[cur[1]] = arg
                instruction_pointer += 1
            case "add":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] += arg
                instruction_pointer += 1
            case "mul":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] *= arg
                instruction_pointer += 1
            case "mod":
                arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                if cur[1] not in registers:
                    registers[cur[1]] = 0
                registers[cur[1]] %= arg
                instruction_pointer += 1
            case "rcv":
                registers[cur[1]] = 105#receive_q.get()
                # if lock.acquire(True):
                #     print(index, f"Received: {registers[cur[1]]}")
                #     lock.release()
                instruction_pointer += 1
            case "jgz":
                if cur[1] in registers and registers[cur[1]] > 0:
                    arg = int(cur[2]) if is_integer_negative_support(cur[2]) else registers[cur[2]]
                    instruction_pointer += arg
                else:
                    instruction_pointer += 1
    if lock.acquire(True):
        print(index, send_count, instruction_pointer)
        lock.release()
    return

if __name__ == "__main__":
    left = Queue()
    right = Queue()
    lock = Lock()
    process_1 = Process(target=run_program, args=(0, {"p": 0}, 0, deepcopy(instr), left, right, lock))
    process_2 = Process(target=run_program, args=(1, {"p": 1}, 0, deepcopy(instr), right, left, lock))
    freeze_support()
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()

