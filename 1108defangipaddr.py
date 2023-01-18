# 4/24/21

from typing import List


class Solution:

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


def test_defangIPaddr():
    solution = Solution()
    assert solution.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"