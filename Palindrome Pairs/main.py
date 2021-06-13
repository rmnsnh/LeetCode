from typing import List
from typing import Tuple

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dict = {}
        ret = []
        for index, word in enumerate(words):
            dict[word] = index
        for wordindex, word in enumerate(words):
            fh = word[:]
            sh = ""
            while len(fh) >= len(sh):

            mid = 
        # for wordindex, word in enumerate(words):
        #     for index in range(len(word) - 1, (len(word) // 2) - 1, -1):
        #         #even palindrome
        #         # print("even")
        #         fh = word[:index + 1][::-1]
        #         sh = word[index + 1:]
        #         # print(fh)
        #         # print(sh)
        #         # print(Solution.palinCheck(fh, sh))
        #         if fh.startswith(sh):
        #             oth = dict.get(fh[len(sh):], -1)
        #             if oth != -1 and oth != wordindex:
        #                 ret.append((wordindex, oth))
        #         # print()
        #     # print()
        #     for index in range(len(word) - 1, (len(word) // 2) - 1, -1):
        #         #odd palindrome
        #         # print("odd")
        #         fh = word[:index][::-1]
        #         sh = word[index + 1:]
        #         # print(fh)
        #         # print(sh)
        #         if fh.startswith(sh):
        #             oth = dict.get(fh[len(sh):], -1)
        #             if oth != -1 and oth != wordindex:
        #                 ret.append((wordindex, oth))
        #         # print(word[index])
        #     # print("BREAK")
        # # print(dict.get('bat', -1))
        return ret
    
    # def palinCheck(st1, st2):
    #     return (st1.startswith(st2), st1[len(st2):])

s = Solution()
print(s.palindromePairs(["raceca", "ar", "racec", "car"]))
print(s.palindromePairs(["civic", "", "race","car"]))
print(s.palindromePairs(["cabba","c"]))
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(s.palindromePairs(["bat","tab","cat"]))
print(s.palindromePairs(["a",""]))