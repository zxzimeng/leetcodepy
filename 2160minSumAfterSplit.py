
class Solution:
    def minimumSum(self, num: int) -> int:
        tens_list = list(str(num))
        tens_list.sort()

        num1 = int(tens_list[0])*10 + int(tens_list[2])
        num2 = int(tens_list[1])*10 + int(tens_list[3])

        return num1+num2

def test_():
    testfunc = Solution().minimumSum
    assert testfunc(2932) == 52
    assert testfunc(4009) == 13
