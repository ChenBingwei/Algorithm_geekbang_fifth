def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    for k in range(m + n - 1, -1, -1):
        if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1


if __name__ == '__main__':
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3
    expected_nums = [1, 2, 2, 3, 5, 6]

    merge(nums1, m, nums2, n)
    assert nums1 == expected_nums
