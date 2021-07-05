from typing import List

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return sum(Solution.recurse(n)) % 1000000007
        # count = [1] * 5
        # while n != 1:
        #     count = [count[1] + count[2] + count[4], count[0] + count[2], count[1] + count[3], count[2], count[2] + count[3]]
        #     print(count)
        #     n -= 1
        # return sum(count) % 1000000007
    
    def recurse(n: int) -> List[int]:
        if n == 1:
            return [1] * 5
        count = Solution.recurse(n - 1)
        return [count[1] + count[2] + count[4], count[0] + count[2], count[1] + count[3], count[2], count[2] + count[3]]

s = Solution()
print(s.countVowelPermutation(1))
print(s.countVowelPermutation(2))
print(s.countVowelPermutation(5))
