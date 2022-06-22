from os import remove
from typing import List


class Solution:
    def checkPalindrome(self, s: List):
        if list(reversed(s)) == s:
            return True

    def validPalindrome(self, s: str) -> bool:
        has_removed = False
        palin_list = list(s)

        if self.checkPalindrome(list(s)):
            return True

        for i, x in enumerate(palin_list):
            print(i, x, palin_list, palin_list[-(i+1)])
            if x == palin_list[-(i+1)]:
                continue

            removed_list = palin_list.copy()
            del removed_list[i]
            if self.checkPalindrome(removed_list):
                return True
            else:
                removed_list = palin_list.copy()
                del removed_list[-(i+1)]
                if self.checkPalindrome(removed_list):
                    return True
                return False

        return True




def test_():
    testfunc = Solution().validPalindrome
    assert testfunc("aba") == True
    assert testfunc("abca") == True
    assert testfunc("abc") == False
    assert testfunc("deeee") == True
    assert testfunc("bbbb") == True
    assert testfunc("aaaxa") == True