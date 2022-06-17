# 4/24/21

class Solution:
     def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in sentence.lower():
                return False
        return True

def test_ ():
    solution = Solution()
    assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True