# 4/12/21

import os
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)


def test_commonPrefix():
    solution = Solution()
    strs = ["flower", "flow", "fly"]
    assert solution.longestCommonPrefix(strs) == "fl"