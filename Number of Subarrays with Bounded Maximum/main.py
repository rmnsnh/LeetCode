from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        noneChosenCount = 0
        noneChosenArray = []
        ret = 0
        for i, num in enumerate(nums):
            if num > right:
                noneChosenArray.append(noneChosenCount)
                noneChosenCount = 0
                for x in range(0, len(noneChosenArray) - 1):
                    L = noneChosenArray[x]
                    R = sum(noneChosenArray[x + 1:]) + len(noneChosenArray[x + 1:]) - 1
                    ret += L + R + 1 + (L * R)
                noneChosenArray = []
            elif num >= left and num <= right:
                noneChosenArray.append(noneChosenCount)
                noneChosenCount = 0
            else:
                noneChosenCount += 1
        noneChosenArray.append(noneChosenCount)
        for x in range(0, len(noneChosenArray) - 1):
            L = noneChosenArray[x]
            R = sum(noneChosenArray[x + 1:]) + len(noneChosenArray[x + 1:]) - 1
            ret += L + R + 1 + (L * R)
        return ret


s = Solution()
print(s.numSubarrayBoundedMax([2,9,2,5,6], 2, 8)) #7
print(s.numSubarrayBoundedMax([1, 2], 2, 3)) #2
print(s.numSubarrayBoundedMax([1, 2, 1], 2, 3)) #4
print(s.numSubarrayBoundedMax([1, 1, 1, 2, 1, 1, 1], 2, 3)) #16
print(s.numSubarrayBoundedMax([1, 1, 1, 2, 1, 1, 1, 2], 2, 3)) #
print(s.numSubarrayBoundedMax([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1], 2, 3)) #
print(s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)) #3
print(s.numSubarrayBoundedMax([1, 2, 1, 2, 1, 4, 3, 1, 1], 2, 3)) #