def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < n:
        nums[count] = 0
        count += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    expect_nums = [1, 3, 12, 0, 0]
    moveZeroes(nums)
    assert nums == expect_nums
