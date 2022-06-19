from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1]]
    
        if rowIndex <= 1:
            return rows[rowIndex]

        for i in range(rowIndex-1):
            newRow = [1]
            for x in range(len(rows[-1])-1):
                newRow.append(rows[-1][x]+rows[-1][x+1])
            newRow.append(1)
            rows.append(newRow)


        return rows[-1]



def test_():
    testfunc = Solution().getRow
    assert testfunc(3) == [1,3,3,1]
