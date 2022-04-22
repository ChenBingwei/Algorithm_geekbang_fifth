from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        s = s + " "
        op_range_dict = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }
        tokens = []
        op_stack = []
        i_char = ""
        for i in s:
            if i.isdigit():
                i_char += i
                continue
            else:
                if i == " ":
                    if i_char != "":
                        tokens.append(int(i_char))
                        i_char = ""
                    continue
                if i in ["+", "-", "*", "/"]:
                    if i_char != "":
                        tokens.append(int(i_char))
                        i_char = ""
                    while len(op_stack) > 0 and op_range_dict[i] <= op_range_dict[op_stack[-1]]:
                        tokens.append(op_stack.pop())
                    op_stack.append(i)
        while len(op_stack) > 0:
            tokens.append(op_stack.pop())
        return self.evalRPN(tokens)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                y = stack.pop()
                x = stack.pop()
                z = self.cal(x, y, token)
                stack.append(z)
            else:
                stack.append(int(token))
        return stack[-1]

    def cal(self, x, y, op):
        if op == "+": return x + y
        if op == "-": return x - y
        if op == "*": return x * y
        if op == "/": return int(x / y)
        return 0


if __name__ == '__main__':
    s = " 3/2 "
    expect = 1
    assert expect == Solution().calculate(s)
