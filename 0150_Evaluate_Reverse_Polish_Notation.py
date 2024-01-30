from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,  # Corrected order of operands
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y / x),  # Corrected order of operands
        }

        for i in tokens:
            if i in operators:
                a = s.pop()
                b = s.pop()
                res = operators[i](int(a), int(b))
                s.append(res)
            else:
                s.append(int(i))

        return int(s.pop())

