import re


class Solution:

    def inpostfix(self, s: str):
        equation = re.findall(re.compile('(\d+|[^ 0-9])'), s)
        rlist = []
        opStk = []
        ops = ['-', '+', '*', '/']
        opM = ['*', '/']
        opA = ['-', '+']
        for c in equation:
            if c == "(":
                opStk.append(c)
                continue
            elif rlist and c in ops:  #if cur is op
                while c in opM and opStk and opStk[
                        -1] in opM:  #if cur is mult and prev is mult
                    rlist.append(opStk.pop())
                while c in opA and opStk and opStk[
                        -1] in opM:  #if prev is mult and cur is add
                    rlist.append(opStk.pop())
                while c in opA and opStk and opStk[
                        -1] in opA:  #if cur is add prev is add
                    rlist.append(opStk.pop())
                opStk.append(c)
                print(opStk, rlist)
                continue
            elif c == ")":
                # print(opStk)
                while rlist[-1] != "(":
                    rlist.append(opStk.pop())
                rlist.pop()
            else:
                rlist.append(c)

        while opStk:
            rlist.append(opStk.pop())
        return rlist

    def calculate(self, s: str) -> int:
        equation = self.inpostfix(s)
        rl = []
        for c in equation:
            if c in ["*", "/", "+", "-"] and len(rl) >= 2:
                sN = rl.pop()
                fN = rl.pop()
                rl.append(int(eval(str(fN) + c + str(sN))))
            else:
                rl.append(c)
        return rl[-1]


def test_():
    solution = Solution()
    assert solution.calculate("3+2*2") == 7
    assert solution.calculate("3/2") == 1
    assert solution.calculate("14/3*2") == 8
    assert solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24
