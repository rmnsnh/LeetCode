from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {}
        for i, e in enumerate(nums1):
            if e in dic:
                dic[e].append(i)
            else:
                dic[e] = [i]
        p, c, ret = [], [], 0
        for e in nums2:
            pn, cn = [], []
            if e in dic:
                for x in dic[e]:
                    cv = 1
                    for i2, e2 in enumerate(p):
                        if e2 == x - 1:
                            cv = c[i2] + 1
                            break
                    pn.append(x)
                    cn.append(cv)
            ret = max(c + [ret])
            p, c = pn, cn
        return max(c + [ret])

s = Solution()
# print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
# print(s.findLength([0,0,0,0,0], [0,0,0,0,0]))
print(s.findLength([1,0,0,0,1], [1,0,0,1,1]))
