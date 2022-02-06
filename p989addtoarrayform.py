# 4/24/21

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numberAsStr = listToStr = ' '.join([str(elem) for elem in num])
        numberAsStr = numberAsStr.replace(" ", "")
        numberAsInt = int(numberAsStr)
        sumInt = numberAsInt+k
        returnVal = [int(x) for x in str(sumInt)]
        return returnVal


def test_addToArrayForm():
    solution = Solution()
    assert solution.addToArrayForm([1,2,0,0], 34) == [1,2,3,4]