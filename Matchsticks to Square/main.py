from typing import List
from collections import Counter

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        s = s // 4
        return Solution.recurse(s, s, s, s, Counter(matchsticks))
    
    def recurse(s1, s2, s3, s4, counter):
        for match in counter:
            print(match)
        return True



s = Solution()
print(s.makesquare([1,1,2,2,2]))
print(s.makesquare([3,3,3,3,4]))
print(s.makesquare([]))
print(s.makesquare([1,1,1,1]))
