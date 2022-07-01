from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        max_list = nums.copy()
        for _ in range(k):
            max_list[max_list.index(min(max_list))] = -(min(max_list))
        
        return sum(max_list)

def test_():
    testfunc = Solution().largestSumAfterKNegations
    assert testfunc([4,2,3], 1) == 5
    assert testfunc([2,-3,-1,5,-4], 2) == 13
    assert testfunc([3,-1,0,2], 3) == 6
