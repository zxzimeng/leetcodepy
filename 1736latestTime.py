class Solution:
    def maximumTime(self, time: str) -> str:
        hours = list(time[0:2])
        minutes = list(time[3:])

        if time[0:2] == "??":
            hours = "23"
        else:
            for i, x in enumerate(hours):
                if x == "?":
                    if i == 0:
                        if int(hours[1]) > 3:
                            hours[i] = "1"
                        else:
                            hours[i] = "2"
                    if i == 1:
                        if int(hours[0]) == 2:
                            hours[i] = "3"
                        else:
                            hours[i] = "9"
                        
        if time[3:] == "??":
            minutes = "59"
        else: 
            for i, x in enumerate(minutes):
                if x == "?":
                    if i == 0:
                        minutes[i] = "5"
                    if i == 1:
                        minutes[i] = "9"

        return hours[0] + hours[1] + ':' + minutes[0] + minutes[1]

def test_():
    testfunc = Solution().maximumTime
    assert testfunc("2?:?0") == "23:50"
    assert testfunc("0?:3?") == "09:39"
    assert testfunc("1?:22") == "19:22"
