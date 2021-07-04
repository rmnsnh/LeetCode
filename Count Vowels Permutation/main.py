from typing import List

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = [1] * 5
        next = [0] * 5
        while n != 1:
            next = [count[1] + count[2] + count[4], count[0] + count[2], count[1] + count[3], count[2], count[2] + count[3]]
            n -= 1
            count = next
            next = [0] * 5
        return sum(count) % 1000000007

s = Solution()
print(s.countVowelPermutation(1))
print(s.countVowelPermutation(2))
print(s.countVowelPermutation(5))
