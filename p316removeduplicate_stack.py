from typing import Counter

from typing import List


class Solution:

  def removeDuplicateLetters(self, s: str) -> str:
    cnt = Counter(list(s))
    stack = []
    print(cnt)
    for x in s:
      cnt[x] -= 1
      if x in stack:
        continue
      while stack:
        if stack[-1] > x and cnt[stack[-1]] > 0:
          stack.pop()
        else:
          break
      if x not in stack:
        stack.append(x)

    return "".join(stack)


def test_():
  solution = Solution()
  assert solution.removeDuplicateLetters(
      "chzafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm"
  ) == "chzafipuegjlxdqnbsotwrym"

  assert solution.removeDuplicateLetters("cbacdcbc") == "acdb"