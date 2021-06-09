from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # trivial cases
        if len(nums) == 1:
            return nums[0]

        # pull out positive numbers
        pos = [0]
        for i in range(1, len(nums) - 1):
            if nums[i] >= 0:
                pos.append(i)
        pos.append(len(nums) - 1)
        
        #positive summation
        ret = 0
        for i in pos:
            ret += nums[i]

        # figure out which parts do not connect, generate tuples that do not
        tups = []
        for i in range(0, len(pos) - 1):
            if pos[i] + k < pos[i + 1]:
                tups.append((pos[i], pos[i + 1]))

        # dijkstras
        # for every tuple loop and create array
        for tup in tups:
            path = nums[tup[0]:tup[1] + 1]
            # for every array loop and djstras
            short = [0]
            short = short + ([-1] * (len(path) - 1))
            print(path)
            print(short)
            # for every node in djstras loop
            for i in range(0, len(path)):
                for toCheck in range(i + 1, min(len(path) - 1, i + k)):
                    print(toCheck)

        return ret

s = Solution()
print(s.maxResult([1,3], 2)) #4
print(s.maxResult([1,-1,-2,4,-7,3], 2)) #7
print(s.maxResult([10,-5,-2,4,0,3], 3)) #17
print(s.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)) #0
