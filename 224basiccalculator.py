from typing import List


class Solution:

    def pushN(self, stack: List, cn: int) -> None:
        if stack and stack[-1] == '+':
            stack.pop()
            stack.append(cn + stack.pop())
        elif stack and stack[-1] == '-':
            if len(stack) == 1:
                stack.pop()
                stack.append(-cn)
            elif len(stack) >= 2 and stack[-2] == '(':
                stack.pop()
                stack.append(-cn)
            else:
                stack.pop()
                stack.append(stack.pop() - cn)
        else:
            stack.append(cn)

    def calculate(self, s: str) -> int:
        s = s + '$'
        stack = []
        i = 0
        operator = ['+', '-', '(']
        while i < len(s):
            print(stack)
            c = s[i]
            if c in operator:
                stack.append(c)
                i += 1
            elif c == ')':
                i += 1
                temp = stack.pop()
                stack.pop()
                self.pushN(stack, temp)
            elif c.isdecimal():
                cn = 0
                for j in range(i, len(s)):
                    if not s[j].isdecimal():
                        break
                    cn = cn * 10 + int(s[j])
                i = j
                self.pushN(stack, cn)
            else:
                i += 1

        return stack.pop()


s = Solution()
# print(s.calculate('123+39'))


def test_():
    assert s.calculate('2014+2013') == 4027
    assert s.calculate('4024-2') == 4022
    assert s.calculate('7-(5-2)') == 4
    assert s.calculate('7+(-5)') == 2
    assert s.calculate("-2+ 1") == -1
