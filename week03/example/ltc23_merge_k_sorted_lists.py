import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DiyNode:
    def __init__(self, key=0, node=None):
        self.key = key
        self.node = node

    def __lt__(self, other):
        return self.key < other.key


class Solution1:
    def mergeKLists(self, lists):
        p_queue = []
        head = ListNode()
        tail = head
        for l_node in lists:
            if l_node:
                p_queue.append(DiyNode(l_node.val, l_node))
        heapq.heapify(p_queue)
        while p_queue:
            smallest_node = heapq.heappop(p_queue)
            tail.next = smallest_node.node
            tail = smallest_node.node
            if tail.next is None:
                continue
            heapq.heappush(p_queue, DiyNode(tail.next.val, tail.next))
        return head.next


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def empty(self):
        return len(self.heap) == 0

    def push(self, node):
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        pop_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return pop_node

    def _heapify_up(self, p):
        while p > 0:
            if self.heap[p].val < self.heap[(p - 1) // 2].val:
                self.heap[p], self.heap[(p - 1) // 2] = self.heap[(p - 1) // 2], self.heap[p]
                p = (p - 1) // 2
            else:
                break

    def _heapify_down(self, p):
        child = p * 2 + 1
        while child < len(self.heap):
            other = p * 2 + 2
            if (other < len(self.heap)) and (self.heap[other].val < self.heap[child].val):
                child = other

            if self.heap[child].val < self.heap[p].val:
                self.heap[p], self.heap[child] = self.heap[child], self.heap[p]
                p = child
                child = 2 * p + 1
            else:
                break


class Solution2:
    def mergeKLists(self, lists: List) -> ListNode:
        b_heap = BinaryHeap()
        for node in lists:
            if node:
                b_heap.push(node)
        head = ListNode()
        tail = head
        while not b_heap.empty():
            dest_node = b_heap.pop()
            tail.next = dest_node
            tail = dest_node
            if tail.next is None:
                continue
            b_heap.push(tail.next)
        return head.next
