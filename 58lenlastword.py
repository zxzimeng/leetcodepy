# 4/11/21

from typing import List
import re


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        if bool(s and not s.isspace()) == False:
            return 0
        x = s.rstrip()
        matches = re.findall(r'^\w+|\w+$', x)
        print(matches)
        return len(matches[-1])


def test_lengthLastWord():
    solution = Solution()
    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("a") == 1
    assert solution.lengthOfLastWord(" a") == 1
    assert solution.lengthOfLastWord("b a ") == 1
    assert solution.lengthOfLastWord(" ") == 0
    assert solution.lengthOfLastWord("    ") == 0
    assert solution.lengthOfLastWord(" a ") == 1
