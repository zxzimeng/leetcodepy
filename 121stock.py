from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        current_min = 0
        for i, x in enumerate(prices):
            if i == 0:
                profits.append(0)
                current_min = x
                continue
            else:
                profit = x - current_min
                if profit > 0:
                    profits.append(profit)
                else:
                    profits.append(0)
                if x < current_min:
                    current_min = x

        return max(profits)


def test_():
    testfunc = Solution().maxProfit
    assert testfunc([7, 1, 5, 3, 6, 4]) == 5
    assert testfunc([7, 6, 4, 3, 1]) == 0
    assert testfunc([2, 4, 1]) == 2
    assert testfunc([7, 2, 4, 1]) == 2
    assert testfunc([7, 1, 5, 3, 6, 4]) == 5
