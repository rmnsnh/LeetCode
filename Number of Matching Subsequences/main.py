from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ret = []
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                dic[c].append(i)
            else:
                dic[c] = [i]
        for word in words:
            isSub = True
            val = -1
        #     print(word)
            for i, c in enumerate(word):
                val = dic.get(c, -2)
                print(val)
                print(c)
                print(i)
                print()
            #     # if val == -2 or i < val:
            #     if val == -2:
            #         isSub = False
            #         break
            #     # val = i
            print(isSub)
            print()
            if isSub:
                ret.append(word)
        return ret

s = Solution()
print(s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
print(s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))