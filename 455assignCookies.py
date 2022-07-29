from this import d
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        g.sort()
        s.sort()

        for x in g:
            for i, j in enumerate(s):
                if j >= x:
                    content += 1
                    s = s[i+1:]
                    break

        return content

def test_():
    testfunc = Solution().findContentChildren
    assert testfunc([1, 2, 3], [1, 1]) == 1
    assert testfunc([1, 2], [1, 2, 3]) == 2
    assert testfunc([1, 2, 3], []) == 0
    assert testfunc([10, 9, 8, 7], [5, 6, 7, 8]) == 2
