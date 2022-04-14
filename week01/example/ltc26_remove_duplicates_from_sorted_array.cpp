//
// Created by chenbingwei on 2022/4/14.
//
#include <vector>
#include <cassert>

int removeDuplicates(std::vector<int> &nums) {
    int n = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (i == 0 || nums[i] > nums[i - 1]) {
            nums[n] = nums[i];
            n++;
        }
    }
    return n;
}


int main() {
    std::vector<int> nums = {1, 2, 2, 3};
    std::vector<int> expectedNums = {1, 2, 3};

    int k = removeDuplicates(nums);
    assert(k == expectedNums.size());

    for (int i = 0; i < k; i++) {
        assert(nums[i] == expectedNums[i]);
    }
    return 0;
}