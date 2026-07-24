from collections import deque


class Solution:
    def resolve_stack(self, temp):
        if type(temp) == str and len(temp) == 0:
            return
        while True:
            if len(self.stack) <= 1:
                self.stack.append(temp)
                break
            top = self.stack.pop()
            match top:
                case "+":
                    self.stack.append(int(self.stack.pop()) + int(temp))
                    temp = self.stack.pop()
                case "-":
                    self.stack.append((0 if self.stack[-1] == "(" else int(self.stack.pop())) - int(temp))
                    temp = self.stack.pop()
                case default:
                    self.stack.append(top)
                    self.stack.append(temp)
                    break

    def calculate(self, s: str) -> int:
        self.stack = deque()
        pointer = 0
        if s[0] == "-":
            self.stack.append(0)
            self.stack.append("-")
            pointer += 1
        while pointer < len(s):
            character = s[pointer]
            if character == " ":
                pointer += 1
                continue
            current_number = ""
            while character.isnumeric():
                current_number += character
                pointer += 1
                if pointer >= len(s):
                    break
                character = s[pointer]
            self.resolve_stack(current_number)
            match character:
                case ")":
                    current_number = self.stack.pop()
                    assert self.stack.pop() == "("
                    self.resolve_stack(current_number)
                case "+" | "-" | "(":
                    self.stack.append(character)
            pointer += 1
        return int(self.stack[0])

