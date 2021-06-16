from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return Solution.recurse(n, n, "", [])
    
    def recurse(open: int, close: int, sb: str, ret: List[str]) -> List[str]:
        # print(ret)
        # print(sb)
        # print()
        if open + close == 0:
            # print("end")
            # print(ret)
            # print(sb)
            return ret.append(sb)
        if open < close:
            # print("close")
            # print(ret)
            # print(Solution.recurse(open, close - 1, sb + ")", ret))
            Solution.recurse(open, close - 1, sb + ")", ret)
            # ret = ret + Solution.recurse(open, close - 1, sb + ")", ret)
            # ret = [*ret, *Solution.recurse(open, close - 1, str + ")", ret)]
        if open != 0:
            # print("open")
            # print(ret)
            # print(Solution.recurse(open - 1, close, sb + "(", ret))
            Solution.recurse(open - 1, close, sb + "(", ret)
            # ret = ret + Solution.recurse(open - 1, close, sb + "(", ret)
            # ret = [*ret, *Solution.recurse(open - 1, close, str + "(", ret)]
        return ret


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))
print(s.generateParenthesis(6))
print(s.generateParenthesis(7))
print(s.generateParenthesis(8))