from typing import List

dictionaryForObscureNumbersThatNeedNaming = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
}


class Solution:

  def numberToWords(self, num: int) -> str:
    if num == 0:
      return "Zero"
    return self.splitNum(num)

  def splitNum(self, num: int):
    if num <= 20:
      if num != 0:
        return dictionaryForObscureNumbersThatNeedNaming[num]
      else:
        return ''
    if num < 10**2:
      tens = num // 10 * 10
      ones = num % 10
      print(tens, ones)
      if ones == 0:
        return dictionaryForObscureNumbersThatNeedNaming[tens]

      rN = dictionaryForObscureNumbersThatNeedNaming[
          tens] + ' ' + dictionaryForObscureNumbersThatNeedNaming[ones]
      rN = rN.strip()
      return rN
    if num < 10**3:
      hundreds = num // 100
      ones = num % 100
      hundreds = dictionaryForObscureNumbersThatNeedNaming[hundreds]
      ones = self.splitNum(ones)
      rN = hundreds + ' Hundred ' + ones
      rN = rN.strip()
      return rN

    if num < 10**6:
      thousands = num // 1000
      thousands = self.splitNum(thousands)
      ones = num % 1000
      ones = self.splitNum(ones)
      rN = thousands + ' Thousand ' + ones
      rN = rN.strip()
      return rN

    if num < 10**9:
      millions = num // 10**6
      millions = self.splitNum(millions)
      ones = num % 10**6
      ones = self.splitNum(ones)
      rN = millions + ' Million ' + ones
      rN = rN.strip()
      return rN

    if num < 10**12:
      billions = num // 10**9
      billions = self.splitNum(billions)
      ones = num % 10**9
      ones = self.splitNum(ones)
      rN = billions + ' Billion ' + ones
      rN = rN.strip()
      return rN


def test_():
  solution = Solution()
  assert solution.numberToWords(
      1234567891
  ) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
  assert solution.numberToWords(30) == "Thirty"
  assert solution.numberToWords(70) == "Seventy"
  assert solution.numberToWords(100) == "One Hundred"
