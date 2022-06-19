from typing import List


class Solution:

  def maxNumber2(self, numbers: List[int], k: int) -> List[int]:
    if k == 0:
      return [-1]
    stack = []
    i = 0

    # fill stack to reach size k
    while i < len(numbers):
      # if all remain elements have to append, do it now.
      if len(stack) + len(numbers) - i == k:
        #print(
        #    f"i={i}: x = {numbers[i]} push all remaining elements stack = {stack} {numbers[i:]}"
        #)
        stack += numbers[i:]
        break

      # we have enough element, new element is not larger
      if len(stack) == k and numbers[i] <= stack[-1]:
        i += 1
        continue

      # try to pop out existing element, but stop when just enough elements
      while stack and len(stack) + len(
          numbers) - i > k and numbers[i] > stack[-1]:
        stack.pop()
      stack.append(numbers[i])
      #print(f"i={i}: x = {numbers[i]} push stack = {stack}")
      i += 1

    #print(stack)
    stack.append(-1)
    return stack

  def merge(self, numb1, numb2):
    i = 0
    j = 0
    #print(numb1, numb2)
    rStack = []
    while numb1[i] != -1 or numb2[j] != -1:
      iIsLarger = True
      ii = i
      jj = j
      while numb1[ii] != -1 or numb2[jj] != -1:
        if numb1[ii] > numb2[jj]:
          iIsLarger = True
          break
        elif numb1[ii] < numb2[jj]:
          iIsLarger = False
          break
        ii += 1
        jj += 1

      if iIsLarger:
        rStack.append(numb1[i])
        i += 1
      else:
        rStack.append(numb2[j])
        j += 1

    #print(f"stack====={rStack[0:10]}")
    return rStack

  def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    largest = []
    for i in range(63, 75):  #k + 1):
      if i <= len(nums1) and k - i <= len(nums2):
        large1 = self.maxNumber2(nums1, i)
        large2 = self.maxNumber2(nums2, k - i)
        print(f"merge with i={i} {len(large1)} {k-i} {len(large2)}")
        largest = max(self.merge(large1, large2), largest)
    return largest


def test_():
  solution = Solution()
  #assert solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3],
  #                          5) == [9, 8, 6, 5, 3]
  #qassert solution.maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]
  #print(solution.maxNumber2([5, 2, 4, 5, 3, 6, 2], 2))
  #assert 0 == 1
  # assert solution.maxNumber([2, 2, 0, 6, 8, 9, 6], [5, 2, 4, 5, 3, 6, 2],
  #                           7) == [9, 6, 5, 5, 3, 6, 2]
  # solution.maxNumber2([
  #     7, 8, 5, 8, 0, 1, 1, 6, 1, 7, 6, 9, 6, 6, 0, 8, 5, 8, 6, 3, 4, 0, 4, 6, 7,
  #     8, 7, 7, 7, 5, 7, 2, 5, 2, 1, 9, 5, 9, 3, 7, 3, 9, 9, 3, 1, 4, 3, 3, 9, 7,
  #     1, 4, 4, 1, 4, 0, 2, 3, 1, 3, 2, 0, 2, 4, 0, 9, 2, 0, 1, 3, 9, 1, 2, 2, 6,
  #     6, 9, 3, 6, 0
  # ], 10)
  # assert 0 == 1

  assert solution.maxNumber([
      1, 5, 8, 1, 4, 0, 8, 5, 0, 7, 0, 5, 7, 6, 0, 5, 5, 2, 4, 3, 6, 4, 6, 6, 3,
      8, 1, 1, 3, 1, 3, 5, 4, 3, 9, 5, 0, 3, 8, 1, 4, 9, 8, 8, 3, 4, 6, 2, 5, 4,
      1, 1, 4, 6, 5, 2, 3, 6, 3, 5, 4, 3, 0, 7, 2, 5, 1, 5, 3, 3, 8, 2, 2, 7, 6,
      7, 5, 9, 1, 2
  ], [
      7, 8, 5, 8, 0, 1, 1, 6, 1, 7, 6, 9, 6, 6, 0, 8, 5, 8, 6, 3, 4, 0, 4, 6, 7,
      8, 7, 7, 7, 5, 7, 2, 5, 2, 1, 9, 5, 9, 3, 7, 3, 9, 9, 3, 1, 4, 3, 3, 9, 7,
      1, 4, 4, 1, 4, 0, 2, 3, 1, 3, 2, 0, 2, 4, 0, 9, 2, 0, 1, 3, 9, 1, 2, 2, 6,
      6, 9, 3, 6, 0
  ], 80) == [
      9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 6, 4, 6, 6, 3, 8,
      1, 1, 3, 1, 3, 5, 4, 3, 9, 5, 0, 3, 8, 1, 4, 9, 8, 8, 3, 4, 6, 2, 5, 4, 1,
      1, 4, 6, 5, 2, 3, 6, 3, 5, 4, 3, 0, 7, 2, 5, 1, 5, 3, 3, 8, 2, 2, 7, 6, 7,
      5, 9, 1, 2, 0
  ]
