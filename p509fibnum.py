class Solution:

    def fib(self, n: int) -> int:
        s = [0] * 31
        s[1] = 1
        if n <= 2:
            if n == 0:
                return 0
            return 1
        for i in range(2, n + 1):
            print(i)
            s[i] = s[i - 1] + s[i - 2]
        print(s)
        return s[n]


def test_():
    solution = Solution()
    assert solution.fib(3) == 1