from typing import List

class NumArray:
    d = {}
    def __init__(self, nums: List[int]):
        for i, num in enumerate(nums):
            NumArray.d[i] = num

    def update(self, index: int, val: int) -> None:
        NumArray.d[index] = val

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += d[i]
        return sum


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3])
# obj = NumArray(nums)
# obj.update(2,4)
param_2 = obj.sumRange(2,4)