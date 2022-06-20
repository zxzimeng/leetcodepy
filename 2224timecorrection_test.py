class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cu_hours = int(current[0:2])
        cu_minutes = int(current[3:])
        co_hours = int(correct[0:2])
        co_minutes = int(correct[3:])
        print(cu_hours, cu_minutes)
        print(co_hours, co_minutes)
        print(cu_hours*60+cu_minutes, co_hours*60+co_minutes)
        return self.maxTime(cu_hours*60+cu_minutes, co_hours*60+co_minutes, 0)

    def maxTime(self, current, correct, tries):
        print(current, correct, tries)
        if current == correct:
            return tries
        if correct-current >= 60:
            current += 60
            return self.maxTime(current, correct, tries+1)
        elif correct-current >= 15:
            current += 15
            return self.maxTime(current, correct, tries+1)
        elif correct-current >= 5:
            current += 5
            return self.maxTime(current, correct, tries+1)
        else:
            current += 1
            return self.maxTime(current, correct, tries+1)

def test_():
    testfunc = Solution().convertTime
    assert testfunc("02:30", "04:35") == 3
    assert testfunc("11:00", "11:01") == 1
    assert testfunc("09:41", "10:34") == 7
