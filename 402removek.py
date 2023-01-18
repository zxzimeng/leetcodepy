class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        popNumbers = 0
        for c in num:
            print(stack, c, popNumbers)
            if not stack or popNumbers == k:
                stack.append(c)
                continue
            elif stack and stack[-1] <= c:
                stack.append(c)
                continue
            while stack and stack[-1] > c and popNumbers < k:
                stack.pop()
                popNumbers += 1
            stack.append(c)
        for i in range(k - popNumbers):
            stack.pop()
        return str(int("".join(stack)))
        # return stack


def test_():
    solution = Solution()
    assert solution.removeKdigits("1432219", 3) == "1219"
    assert solution.removeKdigits("112", 1) == "11"
