from typing import Counter

from typing import List


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        for x in sorted(set(s)):
            index = s.index(x)
            firstH = s[0:index]
            secondH = s[index + 1:]
            if set(firstH) <= set(secondH):
                print(x)
                print(f"recur:{s[index + 1:].replace(x, '')}")
                return x + self.removeDuplicateLetters(s[index + 1:].replace(
                    x, ''))


def test_():
    solution = Solution()
    assert solution.removeDuplicateLetters(
        "chzafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm"
    ) == "chzafipuegjlxdqnbsotwrym"

    assert solution.removeDuplicateLetters("cbacdcbc") == "acdb"
