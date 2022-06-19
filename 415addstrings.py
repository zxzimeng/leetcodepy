# 4/24/21

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int1 = int(num1)
        int2 = int(num2)
        return str(int1+int2)

def test_addStrings():
    solution = Solution()
    assert solution.addStrings('11', '123') == '134'