# 4/11/21

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numberAsStr = listToStr = ' '.join([str(elem) for elem in digits])
        numberAsStr = numberAsStr.replace(" ", "")
        numberAsInt = int(numberAsStr)
        numberAsInt += 1
        res = [int(x) for x in str(numberAsInt)]
        return res


def test_plusOne():
    solution = Solution()
    assert solution.plusOne([1,2,3,4]) == [1,2,3,4]