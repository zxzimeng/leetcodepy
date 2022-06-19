from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        s = [[1], [1, 1], [1, 2, 1]]
        if numRows <= 3:
            return s[0:numRows]
        for i in range(3, numRows):
            t = []
            for j in range(len(s[i - 1])):
                print(s[i - 1][j])
                if j == 0:
                    t.append(1)
                else:
                    t.append(s[i - 1][j - 1] + s[i - 1][j])
            t.append(1)
            s.append(t)
        print(s)
        return s


def test_():
    solution = Solution()
    assert solution.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
