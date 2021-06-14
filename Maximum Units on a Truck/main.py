from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ret = 0
        while truckSize > 0 and a != []:
            a[0][0] -= 1
            ret += a[0][1]
            truckSize -= 1
            if a[0][0] == 0:
                a = a[1:]
        return ret

s = Solution()
print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))
print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
print(s.maximumUnits([[2,5],[5,10],[4,7],[3,9]], 10))