from typing import List

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         ret = []
#         i = 0
#         while i < len(s):
#             if len(ret) > 0 and s[i] == ret[-1]:
#                  ret.pop()
#             else:
#                 ret.append(s[i])
#             i += 1
#         return ''.join(ret)



from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = [2*ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length!=len(s):
            prev_length=len(s)
            for d in duplicates:
                s=s.replace(d, '')
        return s



s = Solution()
print(s.removeDuplicates("abbaca"))       #ca
print(s.removeDuplicates("azxxzy"))       #ay
print(s.removeDuplicates("aabbccddee"))   #
