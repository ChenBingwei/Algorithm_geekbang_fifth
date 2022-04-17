class Solution:
    def plusOne_myself(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                return digits
            else:
                digits[i] -= 9
                if i == 0:
                    return [1] + digits


if __name__ == '__main__':
    digits = [1, 2, 3, 4, 5]
    expect = [1, 2, 3, 4, 6]
    ret = Solution().plusOne_myself(digits)
    assert ret == expect
