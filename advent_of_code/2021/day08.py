from helper import problem_data
from collections import defaultdict


problem_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc 
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

def solve_subproblem(input_data, output_data):
    digits = []
    # for each letter we have the set of possible mappings
    input_data = ["".join(sorted(x)) for x in input_data]
    output_data = ["".join(sorted(x)) for x in output_data]
    letters = set([chr(ord('a')+i) for i in range(7)])
    mapping = {chr(ord('a')+i): letters for i in range(7)}
    # 2: [1]
    # 3: [7]
    # 4: [4]
    # 5: [2, 3, 5]
    # 6: [0, 6, 9]
    # 7: [8]
    while len(output_data):
        cur = output_data.pop(0)
        match len(cur):
            case 2:
                digits.append(1)
            case 3:
                digits.append(7)
            case 4:
                digits.append(4)
            case 7:
                digits.append(8)
    # while len(input_data):
    #     cur = input_data.pop(0)
    #     l = len(cur)
    #     targ = None
    #     # We need to extract extra information out of 5 and 6 somehow, like we have 2 sixers that 
    #     match l:
    #         case 2:
    #             targ = set(['c', 'f'])
    #         case 3:
    #             targ = set(['a', 'c', 'f'])
    #         case 4:
    #             targ = set(['b', 'c', 'd', 'f'])
    #         case 7:
    #             continue
    #         # case _:
    #         #     temp = set()
    #         #     for letter in cur:
    #         #         temp = temp.union(mapping[letter])
    #         #     pass
    #         #     input_data.append(cur)
    #     if targ:
    #         for m in mapping:
    #             mapping[m] = mapping[m].intersection(targ) if m in cur else mapping[m].difference(targ)
    return digits

counts = defaultdict(int)
for line in problem_data.splitlines():
    inp, outp = line.split(" | ")
    inp = inp.split()
    outp = outp.split()
    digits = solve_subproblem(inp, outp)
    for dig in digits:
        counts[dig] += 1
print(counts[1]+counts[4]+counts[7]+counts[8])
