from typing import List

class Solution:
    def findMinChange(self, change, avaliable):

        if change == 0:
            return True, avaliable

        minChange = [0, 0]

        present5 = avaliable[0] != 0
        present10 = avaliable[1] != 0

        if not (present5 or present10):
            return False, avaliable

        if present10 and change >= 10:
            print("change 10")
            avaliable[1] -= 1
            minChange[1] += 1
            change -= 10

        elif present5 and change >= 5:
            print("change 5")
            avaliable[0] -= 1
            minChange[0] += 1
            change -= 5

        elif not present5 and change == 5:
            return False, avaliable

        return self.findMinChange(change, avaliable)

    def lemonadeChange(self, bills: List[int]) -> bool:
        avaliable = [0, 0, 0]

        for i, x in enumerate(bills):
            if x == 5:
                avaliable[0] += 1
                continue
            if x == 10:
                avaliable[1] += 1
            if x == 20:
                avaliable[2] += 1

            change = x - 5
            print(i, change, avaliable)
            success, remaining = self.findMinChange(change, avaliable)
            if not success:
                return False
            avaliable = remaining
        return True

def test_():
    testfunc = Solution().lemonadeChange
    assert testfunc([5,5,5,10,20]) == True
    assert testfunc([5,5,10,10,20]) == False
