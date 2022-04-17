//
// Created by Opt_c on 2022/4/17.
//

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *reverseList(ListNode *head) {
    ListNode *last = nullptr;
    while (head != nullptr) {
        ListNode *nextHead = head->next;
        head->next = last;
        last = head;
        head = nextHead;
    }
    return last;
}

