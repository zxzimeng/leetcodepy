#5/16/21

from typing import List

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        strList = list(moves)
        x = 0
        y = 0
        for i in strList:
            if i == "U":
                y += 1
            if i == "D":
                y -= 1
            if i == "L":
                x -= 1
            if i == "R":
                x += 1
        if x == 0 and y == 0:
            return True
        return False
    
def test_judgeCircle ():
    solution = Solution()
    assert solution.judgeCircle("UD") == True