from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        ret = []
        for num in reversed(nums):
            temp = bisect.bisect_left(arr, num)
            ret.append(temp)
            arr.insert(temp, num)
        return ret[::-1]


s = Solution()
print(s.countSmaller([5,2,6,1]))     #[2,1,1,0]
print(s.countSmaller([-1]))          #[0]
print(s.countSmaller([-1,-1]))       #[0,0]
