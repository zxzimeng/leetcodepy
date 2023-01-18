class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        sL = list(s)
        cLen = 0
        print(sL)
        for i in range(len(sL)):
            if sL[i] == '(':
                stack.append(i)
            if sL[i] == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                if i - stack[-1] > cLen:
                    cLen = i - stack[-1]
        return cLen


def test_():
    solution = Solution()
    assert solution.longestValidParentheses(")()())") == 4
