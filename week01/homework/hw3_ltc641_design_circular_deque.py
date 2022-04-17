class MyCircularDeque_I:

    def __init__(self, k: int):
        self.capacity = k
        self.deque_list = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque_list.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque_list.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque_list.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque_list.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque_list[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque_list[-1]

    def isEmpty(self) -> bool:
        return not self.deque_list

    def isFull(self) -> bool:
        return self.capacity == len(self.deque_list)
