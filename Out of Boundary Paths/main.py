from typing import List

class Solution:

    directions = [-1, 1]
    rows = 0
    cols = 0

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        Solution.rows = m
        Solution.cols = n
        return Solution.recurse(maxMove, startRow, startColumn)

    def recurse(moves: int, row: int, column: int) -> int:
        # print(moves)
        # print(row)
        # print(column)
        # print()
        if moves == 0:
            return 0
        ret = 0
        for direction in Solution.directions:
            if (direction + row <= 0) or (direction + row >= Solution.rows):
                ret += 1
            else:
                ret += Solution.recurse(moves - 1, row + direction, column)
        for direction in Solution.directions:
            if (direction + column <= 0) or (direction + column >= Solution.cols):
                ret += 1
            else:
                ret += Solution.recurse(moves - 1, row, column + direction)
        return ret

s = Solution()
print(s.findPaths(2, 2, 2, 0, 0))
# print(s.findPaths(1, 3, 3, 0, 1))
# print(s.findPaths(50, 50, 50, 25, 25))