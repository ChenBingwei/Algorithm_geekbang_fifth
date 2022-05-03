//
// Created by BingweiChen on 2022/5/3.
//
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector <vector<int>> permute(vector<int> &nums) {
        n = nums.size();
        used = vector<bool>(n, false);
        recur(nums, 0);
        return ans;


    }

private:
    int n;
    vector<int> a;
    vector<bool> used;
    vector <vector<int>> ans;

    void recur(vector<int> &nums, int pos) {
        if (pos == n) {
            ans.push_back(a);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!used[i]) {
                a.push_back(nums[i]);
                used[i] = true;
                recur(nums, pos + 1);
                used[i] = false;
                a.pop_back();
            }
        }
    }
};