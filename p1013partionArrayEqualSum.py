from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        equal_share = sum(arr)/3

        for i in range(2):
            total = 0
            while arr:
                total += arr[0]
                del arr[0]
                print(total, i)
                if total == equal_share:
                    break

        return sum(arr) == equal_share and len(arr) != 0
            
        




def test_():
    testfunc = Solution().canThreePartsEqualSum
    assert testfunc([0,2,1,-6,6,-7,9,1,2,0,1]) == True
    assert testfunc([0,2,1,-6,6,7,9,-1,2,0,1]) == False
    assert testfunc([3,3,6,5,-2,2,5,1,-9,4]) == True
    assert testfunc([1,-1,1,-1]) == False
    assert testfunc([0, 0, 0, 0]) == True