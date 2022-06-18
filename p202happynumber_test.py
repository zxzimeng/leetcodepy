class Solution:
    def getNewNumber(self, n: int):
        digits = [int(a) for a in str(n)] 
        newNum = 0
        for x in digits:
            newNum += x**2
        return newNum

    def findEnd(self, number: int, alrSeen: list):
        if number == 1:
            return True
        if number in alrSeen:
            return False
        newNum = self.getNewNumber(number)
        alrSeen.append(number)
        return self.findEnd(newNum, alrSeen)

    def isHappy(self, n: int) -> bool:
        return self.findEnd(n, [])
        
        
def test_():
    testfunc = Solution().isHappy
    assert testfunc(2) == False
    assert testfunc(19) == True
    assert testfunc(1) == True