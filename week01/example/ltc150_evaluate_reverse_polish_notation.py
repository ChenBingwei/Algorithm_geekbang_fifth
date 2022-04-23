from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                y = stack.pop()
                x = stack.pop()
                z = self.calc(x, y, token)
                stack.append(z)
            else:
                stack.append(int(token))
        return stack[-1]

    def calc(self, x, y, op):
        if op == "+": return x + y
        if op == "-": return x - y
        if op == "*": return x * y
        if op == "/": return int(x / y) # 需要注意 python 中负数除法的表现与题目不一致
        return 0


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    expect_res = 22
    out = Solution().evalRPN(tokens)
    assert expect_res == out
