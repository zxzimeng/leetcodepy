# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        #O(N**2) solutions
        # for windowsize in range(1, len(nums) + 1):
        #     for i in range(len(nums)):
        #         if sum(nums[i:i + windowsize]) >= target:
        #             return windowsize

        # for windowsize in range(1, len(nums) + 1):
        #     startnumber = nums[0]
        #     startsum = sum(nums[0:windowsize])
        #     if startsum >= target:
        #         return windowsize

        #     for i in range(1, len(nums) - windowsize + 1):
        #         startsum = startsum - startnumber + nums[i + windowsize - 1]
        #         if startsum >= target:
        #             return windowsize
        #         startnumber = nums[i]

        rsum = 0
        size = 999999
        l = 0

        # [1, 4, 4]]

        for r in range(1, len(nums) + 1):
            rsum += nums[r - 1]
            while rsum >= target:
                size = min(size, r - l)
                l += 1
                rsum = sum(nums[l:r])

        if size == 999999:
            return 0

        return size


def test_():
    testfunc = Solution().minSubArrayLen
    # assert testfunc(7, [2, 3, 1, 2, 4, 3]) == 2
    # assert testfunc(4, [1, 4, 4]) == 1
    # assert testfunc(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert testfunc(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8
    # assert testfunc(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2
