from typing import Tuple
import unittest


class Solution:

    def split(self, s: str) -> Tuple[str, str]:
        pyramid = [
            "III", "II", "IV", "IX", "I", "V", "XXX", "XX", "XL", "XC", "X",
            "L", "CCC", "CC", "CD", "CM", "C", "D", "M"
        ]
        for i in pyramid:
            if s.startswith(i):
                return i, s[len(i):]
        return "", ""

    def romanToInt(self, s: str) -> int:
        rs = 0
        diction = {
            "III": 3,
            "II": 2,
            "IV": 4,
            "IX": 9,
            "I": 1,
            "V": 5,
            "XXX": 30,
            "XX": 20,
            "XL": 40,
            "XC": 90,
            "X": 10,
            "L": 50,
            "CCC": 300,
            "CC": 200,
            "CD": 400,
            "CM": 900,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if not s:
            return rs
        proccessed = self.split(s)[0]
        tbproccess = self.split(s)[1]
        rs += diction[proccessed]
        print(proccessed, tbproccess, diction[proccessed])
        return rs + self.romanToInt(tbproccess)


class SolutionTest(unittest.TestCase):

    def test_romanToInt(self):
        solution = Solution()
        self.assertEqual(solution.split("VII"), ("V", "II"))
        self.assertEqual(solution.split("IV"), ("IV", ""))
        self.assertEqual(solution.split("IX"), ("IX", ""))
        self.assertEqual(solution.split("MCMXCIV"), ("M", "CMXCIV"))
        self.assertEqual(solution.split("CMXCIV"), ("CM", "XCIV"))
        self.assertEqual(solution.split("XCIV"), ("XC", "IV"))
        self.assertEqual(solution.split("MXCII"), ("M", "XCII"))

        self.assertEqual(solution.romanToInt("MCMXXVIII"), 1928)


if __name__ == '__main__':
    unittest.main()