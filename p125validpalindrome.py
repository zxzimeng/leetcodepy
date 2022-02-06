# 5/14/21
import string
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char,"")
        s = s.lower()
        sb = s[::-1]
        if sb == s:
            return True
        else:
            return False
        
    
def test_isPalindrome ():
    solution = Solution()
    assert solution.isPalindrome("ab_a") == True