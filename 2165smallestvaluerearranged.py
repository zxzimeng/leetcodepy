class Solution:

    def smallestNumber(self, num: int) -> int:
        p = True

        if num < 0:
            p = False
            num *= -1

        if num == 0:
            return num

        numlist = list(str(num))
        numlist.sort()

        zeros = numlist.count('0')
        numlist = numlist[zeros:]
        minnum = ''

        if p:
            for x in numlist:
                minnum += x
            minnum = int(minnum[0] + '0' * zeros + minnum[1:])
        else:
            numlist.reverse()
            for x in numlist:
                minnum += x
            minnum = -1 * int(minnum + '0' * zeros)

        return minnum


def test_():
    testfunc = Solution().smallestNumber
    assert testfunc(310) == 103
    assert testfunc(-7605) == -7650
