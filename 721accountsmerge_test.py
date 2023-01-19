#LEFT UNCOMOPLETE

#Given a list of accounts where each element accounts[i] is a list of strings,
#where the first element accounts[i][0] is a name,
#and the rest of the elements are emails representing emails of the account.

from typing import List


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        totalmerged = []

        for account in accounts:
            emailstotal = account[1:]

            for otheraccount in accounts:
                mergediwthduplicates = account[1:] + otheraccount[1:]
                mergedwithoutdupplicates = list(set(account[1:] + otheraccount[1:]))
                mergediwthduplicates.sort()
                mergedwithoutdupplicates.sort()

                if mergedwithoutdupplicates != mergediwthduplicates:
                    emailstotal += otheraccount[1:]

            emailstotal = list(set(emailstotal))
            emailstotal.sort()
            emailstotal.insert(0, account[0])

            if emailstotal not in totalmerged:
                totalmerged.append(emailstotal)

        print(totalmerged)
        return totalmerged


def test_():
    testfunc = Solution().accountsMerge

    # assert testfunc([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    #                  ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
    #                  ["John", "johnnybravo@mail.com"]
    #                 ]) == [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    #                        ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

    # assert testfunc([["David", "David0@m.co", "David4@m.co", "David3@m.co"],
    #                  ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
    #                  ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
    #                  ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
    #                  ["David", "David4@m.co", "David1@m.co", "David3@m.co"]
    #                 ]) == [["David", "David0@m.co", "David1@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]

    assert testfunc([["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
                     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
                     ["David", "David1@m.co", "David2@m.co"]]) == [[
                         "David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co",
                         "David5@m.co"
                     ]]

    assert testfunc([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                     ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                     ["John", "johnnybravo@mail.com"]
                    ]) == [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                           ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
