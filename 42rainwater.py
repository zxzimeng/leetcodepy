from ast import Index
from typing import Tuple
from collections import namedtuple

from typing import List

Item = namedtuple('Item', ["index", "height"])


class Solution:

    def trap(self, height: List[int]) -> int:
        s: List[Item] = []
        rWater = 0
        for i in range(len(height)):

            while s and height[i] >= s[-1].height:
                prevH = s[-1].height
                s.pop()
                if s:
                    base = min(s[-1].height, height[i])
                    rWater += (base - prevH) * (i - s[-1].index - 1)
            s.append(Item(i, height[i]))
        return rWater


def test_():
    solution = Solution()
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
