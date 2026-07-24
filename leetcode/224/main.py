from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        n = len(s)
        ptr = 0
        if s[0] == "-":
            stack.append("0")
            stack.append("-")
            ptr += 1
        while ptr < n:
            character = s[ptr]
            temp = ""
            while character.isnumeric():
                temp += character
                ptr += 1
                if ptr >= n:
                    break
                character = s[ptr]
                continue
            if len(temp) > 0:
                while True:
                    if len(stack) <= 1:
                        stack.append(temp)
                        break
                    top = stack.pop()
                    if top == "+":
                        stack.append(str(int(stack.pop()) + int(temp)))
                        temp = stack.pop()
                    elif top == "-":
                        left = stack.pop()
                        if left == "(":
                            stack.append("(")
                            stack.append(str(0 - int(temp)))
                        else:
                            assert left.isnumeric() or (left[0] == "-" and left[1:].isnumeric()), left
                            stack.append(str(int(left) - int(temp)))
                        temp = stack.pop()
                    else:
                        stack.append(top)
                        stack.append(temp)
                        break
            match character:
                case "(":
                    stack.append(character)
                case ")":
                    temp = ""
                    stack.append(character)
                    top = stack.pop()
                    while top != "(":
                        top = stack.pop()
                        if top != "(":
                            temp += top
                    # stack.append(temp)
                    # TODO: temp must be numeric so treat it like the numeric above
                    if len(temp) > 0:
                        # We have a number so maybe we can simplify
                        # Loop and check if u have more to simplify
                        while True:
                            if len(stack) <= 1:
                                stack.append(temp)
                                break
                            top = stack.pop()
                            if top == "+":
                                stack.append(str(int(stack.pop()) + int(temp)))
                                temp = stack.pop()
                            elif top == "-":
                                left = stack.pop()
                                if left == "(":
                                    stack.append("(")
                                    stack.append(str(0 - int(temp)))
                                else:
                                    assert left.isnumeric() or (left[0] == "-" and left[1:].isnumeric()), left
                                    stack.append(str(int(left) - int(temp)))
                                temp = stack.pop()
                            else:
                                stack.append(top)
                                stack.append(temp)
                                break
                case "+":
                    stack.append(character)
                case "-":
                    stack.append(character)
                case " ":
                    pass
                case default:
                    # We are at the end ?
                    continue
            ptr += 1
        assert len(stack) == 1
        return int(stack[0])
