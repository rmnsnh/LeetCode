from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        inc = True
        stringlist = [''] * numRows
        i = 0
        for c in s:
            stringlist[i] = stringlist[i] + c
            if inc:
                i = i + 1
            else:
                i = i - 1
            if i == 0 or i == (numRows - 1):
                inc = not inc
        return "".join(stringlist)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))