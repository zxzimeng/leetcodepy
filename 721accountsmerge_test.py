class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pass


def test_():
    testfunc = Solution().accountsMerge
    assert testfunc([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                     ["John", "johnsmith@mail.com", "john00@mail.com"],
                     ["Mary", "mary@mail.com"],
                     ["John", "johnnybravo@mail.com"]]) == [[
                         "John", "john00@mail.com", "john_newyork@mail.com",
                         "johnsmith@mail.com"
                     ], ["Mary",
                         "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
