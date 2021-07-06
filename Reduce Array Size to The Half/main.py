from typing import List
from collections import Counter

# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         l = len(arr)
#         c = Counter(arr).most_common()
#         i = 0
#         size = 0
#         while size < (l // 2):
#             size += c[i][1]
#             i += 1
#         return i

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        k=list(Counter(arr).values())
        k.sort(reverse=True)
        ans=0
        c=0
        while ans<n//2:
            ans+=k[c]
            c+=1
        return c

s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7]))
print(s.minSetSize([1,9]))
print(s.minSetSize([1000,1000,3,7]))
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))
