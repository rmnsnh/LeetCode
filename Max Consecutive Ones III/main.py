from typing import List
from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        max = 0
        count = 0
        lastOne = 0
        for i, num in enumerate(nums):
            if num == 0:
                if k > 0:
                    k -= 1
                    q.append(i)
                    count += 1
                else:
                    q.append(i)
                    lastOne = q.popleft() + 1
                    count = i - lastOne + 1
            else:
                count += 1
            if count > max:
                max = count
        return max


s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))                  #6
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))  #10