from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i, x in enumerate(nums):
            if i != 0:
                if x > nums[i-1]:
                    continue
                operations += nums[i-1]+1-x
                nums[i] = nums[i-1]+1
        return operations

def test_():
    testfunc = Solution().minOperations
    assert testfunc([1, 1, 1]) == 3
    assert testfunc([1,5,2,4,1]) == 14
    assert testfunc([8]) == 0
