class Solution:

    def sumBase(self, n: int, k: int) -> int:
        return sum([int(x) for x in list(self.convertbase(n, k, {}))])

    def convertbase(self, n, k, knowns):
        if n < k:
            return str(n)
        elif n in knowns:
            return knowns[n]
        else:
            knowns[n] = self.convertbase(n // k, k, knowns) + str(n % k)
            return knowns[n]


def test_():
    testfunc = Solution().sumBase
    assert testfunc(34, 6) == 9
    assert testfunc(10, 10) == 1
