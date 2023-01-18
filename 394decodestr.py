from typing import List, cast


class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            print(stack)
            if c.isdigit():
                if stack and isinstance(stack[-1], int):
                    stack.append(stack.pop() * 10 + int(c))
                else:
                    stack.append(int(c))
            elif c == '[':
                stack.append("")
                continue
            elif c == ']':
                char = stack.pop()
                appC = char * stack.pop()
                if stack and isinstance(stack[-1], str):
                    stack.append(stack.pop() + appC)
                else:
                    stack.append(appC)
                continue
            elif stack and isinstance(stack[-1], str):
                stack.append(stack.pop() + c)
            elif not stack:
                stack.append(c)

        print(stack)
        return "".join(stack)


def test_():
    solution = Solution()
    # assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
    # assert solution.decodeString("3[a2[c]]") == "accaccacc"
    # assert solution.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
    assert solution.decodeString("100[leetcode]") == 0
