from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        l = 0
        s = 0

        # pull out positive numbers
        # figure out which parts do not connect
        # dijkstras

        # while l < len(nums):
            # s += nums[l]
            # choices = nums[l + 1:min(len(nums), l + k + 1)]
            # print(choices)
            # l = l + 1
        return s

s = Solution()
print(s.maxResult([1,-1,-2,4,-7,3], 2)) #7
print(s.maxResult([10,-5,-2,4,0,3], 3)) #17
print(s.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)) #0
