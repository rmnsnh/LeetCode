from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        inc = ""
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in inc:
                    return False
                dic[s[i]] = t[i]
                inc += t[i]
        return True

s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("badc", "baba"))
