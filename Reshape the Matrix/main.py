from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat[0]) * len(mat)
        if size != (r * c) or size % r != 0:
            return mat
        ret = []
        count = 0
        toAdd = []
        for i in (x for line in mat for x in line):
            if count < c:
                toAdd.append(i)
                count += 1
            else:
                ret.append(toAdd)
                toAdd = [i]
                count = 1
        ret.append(toAdd)
        return ret

s = Solution()
print(s.matrixReshape([[1,2],[3,4]],1,4))
print(s.matrixReshape([[1,2],[3,4]],2,4))
