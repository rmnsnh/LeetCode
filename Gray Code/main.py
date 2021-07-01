from typing import List

class Solution:

    maxBit = 0
    twos = [2 ** x for x in range(0, 17)]

    def grayCode(self, n: int) -> List[int]:
        Solution.maxBit = n
        return Solution.recurse(0, {0})

    def recurse(n: int, s) -> List[int]:
        if len(s) == (2 ** Solution.maxBit):
            for i in range(0, Solution.maxBit):
                if (n ^ Solution.twos[i]) == 0:
                    return [0]
            return None
        for i in range(0, Solution.maxBit):
            toAdd = n ^ Solution.twos[i]
            if toAdd in s:
                continue
            else:
                s.add(toAdd)
                ret = Solution.recurse(toAdd, s)
                if ret:
                    ret.append(toAdd)
                    return ret
                else:
                    s.discard(toAdd)
        return None

s = Solution()
print(s.grayCode(1))
print(s.grayCode(2))
print(s.grayCode(3))
print(s.grayCode(4))