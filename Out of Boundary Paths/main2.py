from typing import List

class Solution:
    directions = [-1, 1]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        count = 0
        this = [[0]*n for i in range(0, m)]
        next = [[0]*n for i in range(0, m)]
        this[startRow][startColumn] = 1
        for i in range(0, maxMove):
            for x, row in enumerate(this):
                for y, val in enumerate(row):
                    if val == 0:
                        continue
                    else:
                        for d in Solution.directions:
                            if (d + y >= n) or (d + y < 0):
                                count += val
                            else:
                                next[x][d + y] += val                               
                        for d in Solution.directions:
                            if (d + x >= m) or (d + x < 0):
                                count += val
                            else:
                                next[d + x][y] += val
            count = count % 7000000000
            this = next
            next = [[0]*n for i in range(0, m)]
        return count

s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))
print(s.findPaths(3, 3, 1, 1, 1))
print(s.findPaths(3, 3, 2, 1, 1))
print(s.findPaths(3, 3, 3, 1, 1))
print(s.findPaths(1, 3, 3, 0, 1))
print(s.findPaths(1, 3, 1, 0, 1))
print(s.findPaths(50, 50, 50, 25, 25))