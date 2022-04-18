class MinStack:

    def __init__(self):
        self.stack = list()
        self.preMin_stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.preMin_stack:
            self.preMin_stack.append(min(self.preMin_stack[-1], val))
        else:
            self.preMin_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.preMin_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.preMin_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    obj = MinStack()
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.push(6)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
