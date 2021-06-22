from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ret = []
        dic = {}
        for i, c in enumerate(s):
            dic[c] = i
        val = -1
        for word in words:
            isSub = True
            print(word)
            for i, c in enumerate(word):
                val = dic.get(c, -2)
                print(val)
                print(c)
                print(i)
                print()
                if val == -2:
                    continue
                elif i < val:
                    isSub = False
                    break
                val = i
            print(isSub)
            if isSub:
                ret.append(word)
        return ret

s = Solution()
print(s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
print(s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))