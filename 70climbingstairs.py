class Solution:

    def climbStairs(self, n: int) -> int:
        s = [0] * 46
        s[0] = 0
        s[1] = 1
        s[2] = 2
        if n <= 2:
            return s[n]
        for i in range(3, n + 1):
            s[i] = s[i - 1] + s[i - 2]
        return max(s)


def test_():
    solution = Solution()
    assert solution.climbStairs(3) == 2