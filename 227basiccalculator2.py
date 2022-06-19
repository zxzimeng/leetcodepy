class Solution:

  def genInt(self, l: str) -> list:
    listN = []
    curN = 0
    for c in l:
      if c == '$':
        listN.append(curN)
        break
      if c.isdecimal():
        curN = curN * 10 + int(c)
      elif c == ' ':
        continue
      else:
        listN.append(curN)
        curN = 0
        listN.append(c)
    return listN

  def calculate(self, s: str) -> int:
    stack = []
    listN = self.genInt(s + '$')
    for x in listN:
      if stack and stack[-1] == '*':
        stack.pop()
        temp = stack.pop()
        stack.append(temp * x)
      elif stack and stack[-1] == '/':
        stack.pop()
        temp = stack.pop()
        stack.append(temp // x)
      else:
        stack.append(x)
    sign = 1
    result = 0
    for x in stack:
      if x == '+':
        sign = 1
      elif x == '-':
        sign = -1
      else:
        result += x * sign

    print(result)
    return result


def test_():
  solution = Solution()
  assert solution.calculate("1+4*4/8-4*5") == 3
