from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ret = 0
        key = [[] for i in range(0, 26)]
        for i, c in enumerate(s):
            key[ord(c) % 97].append(i)
        for word in words:
            isSub = True
            val = -1
            upto = [0] * 26
            # print(word)
            # print()
            for c in word:
                l = key[ord(c) % 97]
                # print(val)
                # print(c)
                # print(i)
                # print(l)
                # print(p)

                isNotFound = True
                while len(l) > upto[ord(c) % 97]:
                    p = upto[ord(c) % 97]
                    v = l[p]
                    if v > val:
                        val = v
                        upto[ord(c) % 97] = p + 1
                        isNotFound = False
                        break
                    upto[ord(c) % 97] = p + 1
                if isNotFound:
                    isSub = False
                    break
            # print(isSub)
            # print()
            if isSub:
                ret += 1
        return ret

s = Solution()
print(s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
print(s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))


                # # if len(l) <= p:
                # #     isSub = False
                # #     isSub2 = False
                # #     break
                #     v = l[p]
                #     print(v)
                # # if v <= val:
                # #     isSub = False
                # #     isSub2 = False
                # #     break                
                # # print()
                # # print(v)
                # # print()
                #     # val = v
                #     upto[ord(c) % 97] = p + 1

                
                # # if len(l) <= p:
                # #     isSub = False
                # #     isSub2 = False
                # #     break
                # # v = l[p]
                # # if v <= val:
                # #     isSub = False
                # #     isSub2 = False
                # #     break                
                # # print()
                # # print(v)
                # # print()
                # # val = v
                # # upto[ord(c) % 97] = p + 1