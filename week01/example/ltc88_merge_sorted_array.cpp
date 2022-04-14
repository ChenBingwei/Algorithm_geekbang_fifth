//
// Created by chenbingwei on 2022/4/14.
//
#include <vector>
#include <cassert>

using namespace std;


void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < m || j < n) {
        if (j >= n || (i < m && nums1[i] < nums2[j])) {
            result.push_back(nums1[i]);
            i++;
        } else {
            result.push_back(nums2[j]);
            j++;
        }
    }
    nums1 = result;
}

void merge_reverse(vector<int> &nums1, int m, vector<int> &nums2, int n) {

    int i = m - 1;
    int j = n - 1;
    for (int k = m + n - 1; k >= 0; k--) {
        if (j < 0 || (i > 0 && nums1[i] > nums2[j])) {
            nums1[k] = nums1[i];
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
    }
}

int main() {
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    vector<int> nums2 = {2, 5, 6};
    int m = 3, n = 3;
    vector<int> expectedNums = {1, 2, 2, 3, 5, 6};

    merge_reverse(nums1, m, nums2, n);
    assert(nums1 == expectedNums);

    return 0;
}