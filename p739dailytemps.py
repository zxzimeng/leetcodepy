from typing import List


class Solution:

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    rL = [0] * len(temperatures)
    for i in range(len(temperatures)):
      if not stack:
        stack.append(i)
        continue
      while stack and temperatures[stack[-1]] < temperatures[i]:
        rL[stack[-1]] = i - stack[-1]
        stack.pop()
      stack.append(i)

    print(rL)
    return rL


def test_():
  solution = Solution()
  assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76,
                                     73]) == [1, 1, 4, 2, 1, 1, 0, 0]
  assert solution.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100,
                                     70]) == [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
