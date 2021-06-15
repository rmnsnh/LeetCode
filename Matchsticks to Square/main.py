from typing import List
from collections import Counter
import copy

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        s = s // 4
        return Solution.recurse([s, s, s, s], Counter(matchsticks))
    
    def recurse(sarr: List[int], counter: Counter[int]):
        # print(counter)
        if sum(sarr) == 0 and len(counter.keys()) == 0:
            return True
        for matchSize, count in counter.items():
            for i, sideSize in enumerate(sarr):
                if sideSize in sarr[0:i] or sideSize < matchSize:
                    continue
                counterPass = copy.deepcopy(counter)
                sarrPass = copy.deepcopy(sarr)
                sarrPass[i] = sideSize - matchSize
                if count == 1:
                    del counterPass[matchSize]
                else:
                    counterPass[matchSize] -= 1
                if Solution.recurse(sarrPass, counterPass):
                    return True
                # print(size)
                # print(count)
                # counter[size] -= 1
                # print(counter)
        return False



s = Solution()
print(s.makesquare([1,1,2,2,2]))    #true
print(s.makesquare([1,2,2,2]))      #false
print(s.makesquare([2,2,2,2,3]))    #false
print(s.makesquare([3,3,3,3,4]))    #false
print(s.makesquare([]))             #true
print(s.makesquare([1,1,1,1]))      #true
