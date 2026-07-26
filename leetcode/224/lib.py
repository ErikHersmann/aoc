from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        pointer = 0
        negation = deque()
        is_negated = False
        next_number_is_negated = False
        total = 0
        while pointer < len(s):
            character = s[pointer]
            match character:
                case ")":
                    if negation.pop() == "-":
                        is_negated = not is_negated
                case "(":
                    negation.append("+" if not next_number_is_negated else "-")
                    if next_number_is_negated:
                        is_negated = not is_negated
                        next_number_is_negated = False
                case "+" | " ":
                    pass
                case "-":
                    next_number_is_negated = True
                case default:
                    temp = ""
                    while pointer < len(s) and s[pointer].isnumeric():
                        temp += s[pointer]
                        pointer += 1
                    total += (-1 if is_negated ^ next_number_is_negated == 1 else 1)* int(temp)
                    next_number_is_negated =  False
                    continue
            pointer += 1
        return total

