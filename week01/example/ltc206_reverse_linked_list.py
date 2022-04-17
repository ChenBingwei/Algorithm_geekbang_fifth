import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    last = None
    while head:
        next_head = head.next
        head.next = last

        last = head
        head = next_head
    return last


# --------------debug---------------------
def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == '__main__':
    listnode_list = [
        "[1, 2, 3, 4, 5]",
        "[]"
    ]
    expect_list = [
        [5, 4, 3, 2, 1],
        []
    ]
    for i, line in enumerate(listnode_list):
        head = stringToListNode(line)
        ret = reverseList(head)
        out = listNodeToString(ret)
        assert expect_list[i] == stringToIntegerList(out)
