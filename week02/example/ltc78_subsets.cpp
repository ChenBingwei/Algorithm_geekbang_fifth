//
// Created by chenbingwei on 2022/4/29.
//

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int> &nums) {
        recur(nums, 0);
        return ans;
    }

private:
    vector<vector<int>> ans;
    vector<int> subset;

    void recur(vector<int> &nums, int i) {
        if (i == nums.size()) {
            ans.push_back(subset);
            return;
        }

        recur(nums, i + 1);
        subset.push_back(nums[i]);
        recur(nums, i + 1);
        subset.pop_back();

    }
};
