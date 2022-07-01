from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxesLeft = truckSize

        boxSizes = [x[1] for x in boxTypes]
        boxRemaining = [x[0] for x in boxTypes]

        print(boxSizes, boxRemaining, boxesLeft)
        maxBox = 0

        while boxesLeft != 0:
            print(boxesLeft, maxBox, boxSizes, boxRemaining)
            if not boxSizes:
                return maxBox
        
            maxSize = boxSizes.index(max(boxSizes))
            amount = boxRemaining[maxSize]
            if amount <= boxesLeft:
                maxBox += boxSizes[maxSize]*amount
                boxesLeft -= amount
                del boxRemaining[maxSize]
                del boxSizes[maxSize
                ]
            else:
                return maxBox + (boxSizes[maxSize]*boxesLeft)


        return maxBox

def test_():
    testfunc = Solution().maximumUnits
    assert testfunc([[1,3],[2,2],[3,1]], 4) == 8
    assert testfunc([[5,10],[2,5],[4,7],[3,9]], 10) == 91
    assert testfunc([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35) == 76
