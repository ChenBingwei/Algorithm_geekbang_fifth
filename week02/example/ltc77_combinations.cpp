//
// Created by chenbingwei on 2022/4/29.
//
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        this->n = n;
        this->k = k;
        recur(1);
        return ans;

    }

private:
    vector<vector<int>> ans;
    vector<int> sub_combine;
    int n;
    int k;

    void recur(int i) {
        if (sub_combine.size() + (n - i + 1) < k) {
            return;
        }
        if (sub_combine.size() == k) {
            ans.push_back(sub_combine);
            return;
        }
        if (i > n) {
            return;
        }

        // 不选自己
        recur(i + 1);
        // 选自己
        sub_combine.push_back(i);
        recur(i + 1);
        sub_combine.pop_back();

    }

};