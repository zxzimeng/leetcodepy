class Solution:

    def secondHighest(self, s: str) -> int:
        numbers = []
        for i in s:
            if i.isdigit():
                numbers.append(int(i))
        numbers_single = set(numbers)
        numbers_ordered = list(numbers_single)
        numbers_ordered.sort()
        if len(numbers_ordered) > 1:
            return numbers_ordered[-2]
        return -1


def test_():
    testfunc = Solution().secondHighest
    assert testfunc("dfa12321afd") == 2
    assert testfunc("abc1111") == -1
