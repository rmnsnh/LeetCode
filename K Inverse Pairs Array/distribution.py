from typing import List
from itertools import permutations
from collections import Counter

class Solution:
    def count(l):
        ret = 0
        for i, num in enumerate(l):
            for x in range(i + 1, len(l)):
                if num > l[x]:
                    ret += 1
        return ret

    def kInversePairs(self, n: int, k: int) -> None:
        a = list(permutations(range(1, n)))
        result = list(map(Solution.count, a))
        print(Counter(result))
        print(len(Counter(result).keys()))
        # print(a)
        print(result)

s = Solution()
s.kInversePairs(1, 1)
s.kInversePairs(2, 1)
s.kInversePairs(3, 1)
s.kInversePairs(4, 1)
s.kInversePairs(5, 1)
s.kInversePairs(6, 1)
s.kInversePairs(7, 1)
s.kInversePairs(8, 1)