from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        increasing = True
        decreasing = True
        startOfDown = 0
        ret = 0
        CandyPerChild = 1
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                if decreasing:
                    size = (i - startOfDown)
                    if size > CandyPerChild:
                        ret += ((size * (size + 1)) // 2)
                        CandyPerChild = 1
                    else:
                        ret += (((size * (size + 1)) // 2) + ((CandyPerChild - size) * size))
                        CandyPerChild = CandyPerChild - size + 1
                else: 
                    CandyPerChild += 1
                    ret += CandyPerChild
                increasing = True
                decreasing = False
            elif ratings[i-1] > ratings[i]:
                if increasing:
                    startOfDown = i - 1
                decreasing = True
                increasing = False
            else:
                if decreasing:
                    size = (i - startOfDown)
                    if size > CandyPerChild:
                        ret += ((size * (size + 1)) // 2)
                        CandyPerChild = 2
                    else:
                        ret += (((size * (size + 1)) // 2) + ((CandyPerChild - size) * size))
                        CandyPerChild = CandyPerChild - size + 1
                else:
                    if CandyPerChild > 1:
                        CandyPerChild -= 1
                    ret += CandyPerChild
                increasing = False
                decreasing = False
        print(ret)
        if increasing:
            return ret + CandyPerChild + 1
        elif decreasing:
            print(startOfDown)
            print(i)
            size = (i - startOfDown + 1)
            if size > CandyPerChild:
                ret += ((size * (size + 1)) // 2)
            else:
                ret += (((size * (size + 1)) // 2) + ((CandyPerChild - size) * size))
            return ret
        else:
            if CandyPerChild > 1:
                CandyPerChild -= 1
            return ret + CandyPerChild


s = Solution()
# print(s.candy([1,3]))
# print(s.candy([1,3,2]))
# print(s.candy([1,3,2,2]))
print(s.candy([1,3,2,2,1]))
# print(s.candy([1,0,2]))                 #5
# print(s.candy([1,2,2]))                 #4
# print(s.candy([1,2]))                   #3
# print(s.candy([2,1]))                   #3
# print(s.candy([100,99,98,97,96]))       #15
# print(s.candy([1,2,100]))               #6
# print(s.candy([1,2,100,99,98]))         #9
# print(s.candy([1,2,100,99,98,97,96]))     #18    
# print(s.candy([1,2,100,99,98,97,96,97]))  #20
# print(s.candy([1,2,100,99,98,97,96,97,96]))  #21
# print(s.candy([1,2,3,4,5,100,99]))        #26    