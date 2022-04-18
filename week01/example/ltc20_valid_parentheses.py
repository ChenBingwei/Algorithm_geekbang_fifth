class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if (i == ')' and stack[-1] != '(') \
                        or (i == ']' and stack[-1] != '[') \
                        or (i == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    str_list = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    expect_res = [True, True, False, False, True]
    for i in range(len(str_list)):
        assert Solution().isValid(str_list[i]) == expect_res[i]
