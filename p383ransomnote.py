# 5/14/21

from typing import List 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i],'',1)
            else:
                return False
        return True
            
            
def test_canConstruct ():
    solution = Solution()
    assert solution.canConstruct("aab","baa") == True 