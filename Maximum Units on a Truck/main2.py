from typing import List
import bisect

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         added = []
#         while truckSize != 0 and boxTypes != []:
#             for box in boxTypes:
#                 while box[0] != 0 and truckSize != 0:
#                     box[0] -= 1
#                     truckSize -= 1
#                     bisect.insort(added, box[1])
#                     if box[0] == 0:
#                         boxTypes = boxTypes[1:]
#         for box in boxTypes:
#             if box[1] > added[0]:
#                 while box[0] != 0:
#                     box[0] -= 1
#                     added = added[1:]
#                     bisect.insort(added, box[1])
#         return sum(added)
                #add in a*scending order
            
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
print(s.maximumUnits([[2,5],[4,7],[3,9],[5,10]], 10))
print(s.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))