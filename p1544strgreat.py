from typing import List


class Solution:

  def makeGood(self, s: str) -> str:
    stack = []
    s = s.lower()
    for i in range(len(s)):
      print(i)
      print(len(s))
      if not stack:
        stack.append(s[i])
        continue
      elif len(s) - 1 != i and stack and stack[-1] == s[i] and s[i + 1] == s[i]:
        stack.pop()
        stack.append(s[i])
        continue
      else:
        stack.append(s[i])
      print(stack)
    return "".join(stack)


def test_():
  solution = Solution()
  assert solution.makeGood("leEeetcode") == "leetcode"
  # assert solution.makeGood("abBAcC") == "abbacc"