class Solution:

    def longestBeautifulSubstring(self, word: str) -> int:
        i = 0
        vowels = 'aeiou'
        vowelindex = 0
        maxlength = 0
        print('\n' + str(len(word)))
        while i < len(word):
            letter = word[i]

            if letter == vowels[vowelindex]:
                # print(f"scan started {i}")
                currentlength = 1
                complete = False
                # countprevious = 1
                # print(f"\nfound a")
                while vowelindex <= 4 and (i < len(word) - 1):
                    i += 1
                    letter = word[i]
                    if letter == vowels[vowelindex]:
                        currentlength += 1
                        # countprevious += 1
                        if i == len(word) - 1 and vowelindex == 4:
                            complete = True
                    elif vowelindex == 4:
                        # print(f"same {word[i-1]} for {countprevious} times")
                        # print("end of scan")
                        # print(f"scan ended {i-1}")
                        i -= 1
                        complete = True
                        break
                    elif letter == vowels[vowelindex + 1]:
                        # print(f"same {word[i-1]} for {countprevious} times")
                        # countprevious = 1
                        # print(f"next letter {letter}")
                        currentlength += 1
                        vowelindex += 1
                        if i == len(word) - 1 and vowelindex == 4:
                            complete = True
                    else:
                        # print(f"{letter} not after {word[i-1]}")
                        i -= 1
                        vowelindex = 0
                        break

                if complete:
                    vowelindex = 0
                    maxlength = max(currentlength, maxlength)
                    # print("complete scan")
                    # print(f"total {currentlength}")
            else:
                pass
            i += 1

        return maxlength


def test_():
    testfunc = Solution().longestBeautifulSubstring
    assert testfunc("xaeiuadfaaaaeeeeeiiiiouuuu") == 18
    assert testfunc("aeeeiiiioooauuuaeiou") == 5
    assert testfunc("eoauiauioeioeauuiaoeeuoiauiaoeuaeoiiouaeeiauouioea") == 0
    assert testfunc("aaaaa") == 2
