import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        protect = ListNode(next=head)
        last = protect
        while head:
            # 1.分组（往后走k-1步，找到一组），一组的开头head，结尾end
            end = self._get_end(head, k)
            if end is None:
                break
            next_group_head = end.next

            # 2.一组内部（head到end之间）要反转（调用反转链表）
            self._reverseList(head, next_group_head)

            # 3.更新每组跟前一组，后一组之间的边
            last.next = end
            head.next = next_group_head

            last = head
            head = next_group_head
        return protect.next

    def _get_end(self, head, k):
        """返回走k-1步之后的结点，返回None表示不够k个"""
        while head:
            k -= 1
            if k == 0:
                return head
            head = head.next
        return None

    def _reverseList(self, head, stop):
        """反转链表，在stop位置停止"""
        last = head
        head = head.next
        while head != stop:
            next_head = head.next
            head.next = last

            last = head
            head = next_head


# common tool
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
    list_str = "[1,2,3,4,5]"
    k = 3
    expect_list = [3, 2, 1, 4, 5]

    head = stringToListNode(list_str)
    ret = Solution().reverseKGroup(head, k)
    out = stringToIntegerList(listNodeToString(ret))
    assert expect_list == out
