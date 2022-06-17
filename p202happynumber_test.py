class Solution:
    def getNewNumber(self, n: int):
        newNumber = 0
        for x in list(str(n)):
            newNumber += int(x)**2
        return newNumber

    def isHappy(self, n: int) -> bool:
        alreadySeen = [n]
        
        newNum = self.getNewNumber(n)
        if newNum == 1:
            return True

        while newNum not in alreadySeen:
            if newNum == 1:
                return True
            alreadySeen.append(newNum)
            newNum = self.getNewNumber(newNum)

        return False
        
        
def test_():
    testfunc = Solution().isHappy
    assert testfunc(2) == False
    assert testfunc(19) == True
    assert testfunc(1) == True