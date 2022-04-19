def find_neighbor(k, nums):
    for i in range(1, k):
        min_diff = 2e9 + 1
        pos = 0
        for j in range(0, i):
            diff = abs(nums[i] - nums[j])
            if diff < min_diff:
                min_diff = diff
                pos = j
            elif diff == min_diff:
                min_diff = diff
                if nums[pos] > nums[j]:
                    pos = j
        print("%d %d" % (min_diff, pos + 1))


if __name__ == '__main__':
    # n = int(input())
    # nums_str = input()
    # nums =list(map(int, nums_str.split()))
    find_neighbor(10 ,[4,5,6,1,2,3,7,8,9,10,])
