#Given a list of accounts where each element accounts[i] is a list of strings, 
#where the first element accounts[i][0] is a name, 
#and the rest of the elements are emails representing emails of the account.

from typing import List

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for account in accounts:
            emails = []
            name = ''
            for email in accounts





def test_():
    testfunc = Solution().accountsMerge
    assert testfunc([["John", "johnsmith@mail.com", "john_newyork@mail.com"]["John", "johnsmith@mail.com",
                                                                             "john00@mail.com"],
                     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]
                    ]) == [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                           ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
