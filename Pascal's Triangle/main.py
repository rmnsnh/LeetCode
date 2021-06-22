from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(2, numRows + 1):
            temp = [1]
            if i % 2 == 0:
                for x in range(1, i // 2):
                    temp.append(ret[i - 2][x - 1] + ret[i - 2][x])
                temp = temp + temp[::-1]
            else:
                for x in range(1, (i // 2) + 1):
                    temp.append(ret[i - 2][x - 1] + ret[i - 2][x])
                temp = temp[:-1] + temp[::-1]
            ret.append(temp)
        return ret


s = Solution()
print(s.generate(1))
print(s.generate(2))
print(s.generate(4))
print(s.generate(10))
print(s.generate(30))