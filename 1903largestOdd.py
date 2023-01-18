class Solution:

    def largestOddNumber(self, num: str) -> str:
        for i, x in enumerate(list(num[::-1])):
            print(i, x, num, list(num[::-1]))
            if int(x) % 2 == 1:
                return num[0:(len(num) - 1) - i + 1]

        return ""


def test_():
    testfunc = Solution().largestOddNumber
    assert testfunc("52") == "5"
    assert testfunc("4206") == ""
    assert testfunc("35427") == "35427"
