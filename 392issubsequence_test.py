
class Solution:
    def filterFirst(self, s, t):
        if not s:
            return True
        if not t:
            return False
        elif s[0] == t[0]:
            return self.filterFirst(s[1:], t[1:])
        return self.filterFirst(s, t[1:])

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.filterFirst(s, t)


def test_():
    testfunc = Solution().isSubsequence
    assert testfunc("abc" ,"ahbgdc") == True
    assert testfunc("", "ahgbdc") == True
    assert testfunc("b", "abc") == True