//
// Created by BingweiChen on 2022/5/3.
//
#include <bits/stdc++.h>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode *root) {
        ans = 0;
        depth = 1;
        calc(root);
        return ans;
    }

private:
    int depth;
    int ans;

    void calc(TreeNode *root) {
        if (root == nullptr) return;
        ans = max(ans, depth);
        depth++;
        calc(root->left);
        calc(root->right);
        depth--;
    }
};