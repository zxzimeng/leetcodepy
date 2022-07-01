class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)

        for i, x in enumerate(numStr):
            if x == 9:
                continue
            replace_current = numStr[0:i] + '9' + numStr[i+1:]

            if int(replace_current) > int(numStr):
                return int(replace_current)
        
        return num
        
def test_():
    testfunc = Solution().maximum69Number
    assert testfunc(9669) ==  9969
    assert testfunc(9996) ==  9999
    assert testfunc(9999) ==  9999
