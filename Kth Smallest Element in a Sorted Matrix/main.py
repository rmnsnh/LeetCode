from typing import List
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        dic = {(0,0)}
        sorteda = [(matrix[0][0], 0, 0)]
        start = 0
        # print(k)
        while True:
            e = sorteda.pop(0)
            # print(e)
            # print(start)
            if start == k - 1:
                return e[0]
            start += 1
            if (e[1] + 1, e[2]) not in dic and e[1] + 1 < len(matrix):
                dic.add((e[1] + 1, e[2]))
                bisect.insort(sorteda, (matrix[e[1] + 1][e[2]], e[1] + 1, e[2]))
            if (e[1], e[2] + 1) not in dic and e[2] + 1 < len(matrix):
                dic.add((e[1], e[2] + 1))
                bisect.insort(sorteda, (matrix[e[1]][e[2] + 1], e[1], e[2] + 1))


s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
print(s.kthSmallest([[-5]],1))