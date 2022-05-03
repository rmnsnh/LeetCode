from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and p == "":
            return True
        if p == "":
            return False

        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return Solution.isMatch(self, s[1:], p) or Solution.isMatch(self, s, p[2:])
            return Solution.isMatch(self, s, p[2:])
        if len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.'):
            return Solution.isMatch(self, s[1:], p[1:])
        return False

s = Solution()
print(s.isMatch("ab", ".*"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "aa"))
print(s.isMatch("mississippi", "mis*is*p*."))