class Solution:

    def listInt(self, intlist: list):
        numberstr = ''
        for x in intlist:
            numberstr += x
        return int(numberstr)

    def removeDigit(self, number: str, digit: str) -> str:
        largest = 0
        numberlist = list(number)
        for i, x in enumerate(numberlist):
            if x == digit:
                numberWithRemoved = self.listInt(numberlist[0:i] +
                                                 numberlist[i + 1:])
                if numberWithRemoved > largest:
                    largest = numberWithRemoved
        return str(largest)


def test_():
    testfunc = Solution().removeDigit
    assert testfunc("123", "3") == "12"
    assert testfunc("1231", "1") == "231"
    assert testfunc("551", "5") == "51"