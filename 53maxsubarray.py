from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[:]
        for i in range(len(s) - 2, -1, -1):
            s[i] = max(s[i], s[i] + s[i + 1])
        return max(s)


def test_():
    solution = Solution()
    assert solution.maxSubArray([1, 2, -4, 8, -5]) == -101
