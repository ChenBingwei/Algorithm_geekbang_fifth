//
// Created by Opt_c on 2022/4/17.
//
// https://www.acwing.com/problem/content/description/138/

#include <bits/stdc++.h>

using namespace std;

struct Node {
    int val;
    int idx;
    Node *pre;
    Node *next;
};

const int SIZE = 1000005;
int a[SIZE], ans[SIZE], rk[SIZE], n;
Node *pos[SIZE];

// 双链表插入模板，在node后面插入一个新结点
Node *AddNode(Node *node, int idx) {
    Node *newNode = new Node();
    newNode->val = a[idx];
    newNode->idx = idx;
    node->next->pre = newNode;
    newNode->next = node->next;

    newNode->pre = node;
    node->next = newNode;
    return newNode;

}

// 双链表删除模板
void DeleteNode(Node *node) {
    node->pre->next = node->next;
    node->next->pre = node->pre;
    delete node;
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
        rk[i] = i;
    }
    // rk的含义：rk[i]表示排名第i名的是谁？（是哪个下标）？
    // 有序序列为a[rk[1]], a[rk[2]], a[rk[3]], ...a[rk[n]]
    sort(rk + 1, rk + n + 1, [&](int rki, int rkj) { return a[rki] < a[rkj]; });

    // 保护节点
    Node head{};
    Node tail{};
    head.next = &tail;
    tail.pre = &head;
    head.pre = nullptr;
    tail.next = nullptr;
    for (int i = 1; i <= n; i++) {
        pos[rk[i]] = AddNode(tail.pre, rk[i]);
    }
    for (int i = n; i > 1; i--) {
        Node *curr = pos[i];
        if (curr->pre->pre == nullptr ||
            (curr->next->next != nullptr && a[i] - curr->pre->val > curr->next->val - a[i])) {
            ans[i] = curr->next->idx;
        } else {
            ans[i] = curr->pre->idx;
        }
        DeleteNode(curr);
    }
    for (int i = 2; i <= n; i++) {
        printf("%d %d\n", abs(a[ans[i]] - a[i]), ans[i]);
    }
}
