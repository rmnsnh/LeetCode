from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = nums
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start != end:
            sum = nums[start] + nums[end]
            if sum == target:
                break
            elif sum < target:
                start += 1
            elif sum > target:
                end  -= 1
        if nums[start] == nums[end]:
            f = original.index(nums[start])
            return [f, original[f + 1:].index(nums[end]) + f + 1]
        return [original.index(nums[start]),original.index(nums[end])]

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
