def removeDuplicates(nums):
    n = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i - 1]:
            nums[n] = nums[i]
            n += 1
    return n


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expect_nums = [0, 1, 2, 3, 4]

    k = removeDuplicates(nums)
    assert k == len(expect_nums)
    for i in range(k):
        assert nums[i] == expect_nums[i]
