import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # -100 <= Node.val <= 100
        head = ListNode(val=-101)
        curr = head
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                break
            if list2 is None:
                curr.next = list1
                break

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head.next


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
    ll1 = stringToListNode("[1,2,4]")
    ll2 = stringToListNode("[1,3,4,5]")
    expect_list = [1, 1, 2, 3, 4, 4, 5]
    ret = Solution().mergeTwoLists(ll1, ll2)
    out = stringToIntegerList(listNodeToString(ret))
    assert expect_list == out
