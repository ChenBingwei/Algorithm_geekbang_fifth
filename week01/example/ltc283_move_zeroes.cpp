//
// Created by chenbingwei on 2022/4/14.
//

#include <vector>
#include <cassert>

void moveZeroes(std::vector<int> &nums) {
    int n = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[n] = nums[i];
            n++;
        }
    }
    while (n < nums.size()) {
        nums[n] = 0;
        n++;
    }
}

int main() {
    std::vector<int> nums = {0, 1, 0, 3, 12};
    std::vector<int> expectedNums = {1, 3, 12, 0, 0};

    moveZeroes(nums);
    assert(nums == expectedNums);

    return 0;
}