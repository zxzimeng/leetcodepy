# 5/9/21
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1s = ""
        word2s = ""
        for ele in word1: 
            word1s += ele  
        for ele in word2: 
            word2s += ele       
        if word1s == word2s:
            return True
        if word1s != word2s:
            return False

def test_arrayStringsAreEqual ():
    solution = Solution()
    assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True