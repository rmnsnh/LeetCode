from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        max = bisect.bisect_left(arr, x)
        if max == len(arr):
            return arr[-k:]
        if max == 0:
            return arr[:k]
        if abs(arr[max-1]-x) <= abs(arr[max]-x):
            max -= 1
        min = max
        k -= 1
        while k != 0:
            # print(arr[min])
            # print(arr[max])
            # print(abs(arr[min]-x))
            # print(abs(arr[max]-x))
            # print(min)
            # print(max)
            # print()
            if max == len(arr) - 1:
                min -= k
                break
            elif min == 0:
                max += k
                break
            elif abs(arr[min - 1]-x) <= abs(arr[max + 1]-x):
                min -= 1
            else:
                max += 1
            k -= 1
        return arr[min:max + 1]

s = Solution()
print(s.findClosestElements([1,2,3,4,5],4,3))
print(s.findClosestElements([1,2,4,5],3,3))
print(s.findClosestElements([1,2,40,50],3,3))
print(s.findClosestElements([1,2,3,3,4,5],4,3))
print(s.findClosestElements([1,2,3,4,5],4,6))
print(s.findClosestElements([1,2,3,4,5],5,6))
print(s.findClosestElements([1,1,1,1,1,1,2,3,4,5],4,1))
print(s.findClosestElements([1,2,3,4,5],4,-1))
print(s.findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5))
