import string
class Solution:
    def findShortestTime(self, current_letter, target_letter):
        alphabet = list(string.ascii_lowercase)
        alphabet_two = [x*2 for x in alphabet]
        alphabet_merged = alphabet_two + alphabet
        
        distance_clock_1 = abs(alphabet_merged.index(target_letter) - alphabet_merged.index(current_letter))
        distance_clock_2 = abs(alphabet_merged.index(current_letter*2) - alphabet_merged.index(target_letter))
        distance_clock_3 = abs(alphabet_merged.index(current_letter) - alphabet_merged.index(target_letter*2))
        distance_clock = min(distance_clock_1, distance_clock_2, distance_clock_3)


        return distance_clock

    def minTimeToType(self, word: str) -> int:
        alphabet_list = list(string.ascii_lowercase)
        current_letter = 'a'
        time = 0

        for i, x in enumerate(list(word)):
            if x == current_letter:
                time += 1
            else:
                print(current_letter, x, self.findShortestTime(current_letter, x))
                time += self.findShortestTime(current_letter, x) + 1
            current_letter = x

        return time



def test_():
    testfunc = Solution().minTimeToType
    assert testfunc("abc") == 5
    assert testfunc("bza") == 7
    assert testfunc("zjpc") == 34
