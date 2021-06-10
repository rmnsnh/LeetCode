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
            path = nums[tup[0]:tup[1]] + [0]
            # for every array loop and djstras
            short = [0]
            short = short + ([-1] * (len(path) - 1))

            if len(set(path[1:-1])) <= 1:
                ret += path[1]*((len(path) - 1)//k)
                if (len(path) - 1)%k != 0:
                    ret += path[1]
                continue

            # print(path)
            # print(short)
            # for every node in djstras loop
            i = 0
            while i < len(path):
                # rom = path[i + 1:min(len(path) - 1, i + k) + 1]
                # print(rom)
                # if len(rom) > 0 and max(rom) == rom[-1]:
                #     print('yo')
                #     print(rom[-1])
                #     print(i)
                #     print(min(len(path) - 1, i + k) + 1)
                #     print()
                    # negsum += rom[-1]
                    # i = min(len(path) - 1, i + k) + 1
                    # continue
                for toCheck in range(i + 1, min(len(path) - 1, i + k) + 1):
                    # print(i)
                    # print(path[toCheck])
                    if short[toCheck] == -1 or short[i]+(path[toCheck]*-1) < short[toCheck]:
                        short[toCheck] = short[i]+(path[toCheck]*-1)
                    # print(short)
                i = i + 1
            ret += (-1*short[-1])
        return ret

s = Solution()
print(s.maxResult([1,3], 2)) #4
print()
print(s.maxResult([1,-1,-2,4,-7,3], 2)) #7
print()
print(s.maxResult([10,-5,-2,4,0,3], 3)) #17
print()
print(s.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)) #0
print()
print(s.maxResult([1] + ([-1] * 10) + [1], 3))
print([1] + ([-1] * 10) + [1])
print()
# a = s.maxResult([1] + ([-1] * 10000002) + [1], 1)
# print(a)