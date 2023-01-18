from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> List[str]:
        s.reverse()
        return s


def test_reverseString():
    solution = Solution()
    assert solution.reverseString(["h", "e", "l", "l",
                                   "o"]) == ["o", "l", "l", "e", "h"]
