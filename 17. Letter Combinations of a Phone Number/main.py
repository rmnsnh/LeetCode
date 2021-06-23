from typing import List

class Solution:
    iterate = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        return Solution.recurse(digits, "", [])

    def recurse(digits: str, build: str, ret: List[str]) -> List[str]:
        if digits == "":
            ret.append(build)
            return ret
        for letter in Solution.iterate[int(digits[0]) - 2]:
            Solution.recurse(digits[1:], build + letter, ret)
        return ret

s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))