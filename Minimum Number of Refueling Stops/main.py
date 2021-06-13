from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        print('hi')


s = Solution()
print(s.minRefuelStops(1, 1, []))
print(s.minRefuelStops(100, 1, [[10,100]]))
print(s.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))
