class Solution:

    def myAtoi3(self, s: str) -> int:
        numbers = {f"{i}": i for i in range(10)}
        rNum = 0
        for x in s:
            if x not in numbers:
                break
            rNum = rNum * 10 + numbers[x]

        return rNum

    def myAtoi2(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        elif s[0] == '-':
            return -self.myAtoi3(s[1:])
        elif s[0] == '+':
            return self.myAtoi3(s[1:])
        return self.myAtoi3(s)

    def myAtoi(self, s: str) -> int:
        num = self.myAtoi2(s)
        num = min(num, 2**31 - 1)
        num = max(num, -2**31)

        return num


def test_():
    solution = Solution()
    assert solution.myAtoi("+-12") == 0
