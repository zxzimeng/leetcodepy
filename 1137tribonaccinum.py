class Solution:

    def tribonacci(self, n: int) -> int:
        s = [0] * 31
        s[0] = 0
        s[1] = 1
        s[2] = 1
        if n <= 2:
            return s[n]
        for i in range(3, n + 1):
            print(i)
            s[i] = s[i - 1] + s[i - 2] + s[i - 3]
        print(s)
        return s[n]


def test_():
    solution = Solution()
    assert solution.tribonacci(3) == 3