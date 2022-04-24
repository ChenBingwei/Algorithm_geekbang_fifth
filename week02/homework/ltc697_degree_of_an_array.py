from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_freq_dict = {}
        for i, num in enumerate(nums):
            # 列表默认为[频次，起始，终止]
            num_freq_dict.setdefault(num, [0, i, i])
            num_freq_dict[num][0] += 1
            num_freq_dict[num][2] = i

        max_freq = 0
        min_len = len(nums)
        for k, v_list in num_freq_dict.items():
            freq = v_list[0]
            tmp_len = v_list[2] - v_list[1] + 1
            if freq > max_freq:
                max_freq = v_list[0]
                min_len = tmp_len
            elif freq == max_freq:
                min_len = min(min_len, tmp_len)
        return min_len


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 4, 2]
    expect_out = 6
    assert expect_out == Solution().findShortestSubArray(nums)
