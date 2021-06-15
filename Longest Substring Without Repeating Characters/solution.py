from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        lofd = []
        for c in s:
            #add to each dictionary if not there, if it is, remove that instance
            # print(c)
            throwOut, tokeep = Solution.partition(lambda dict: dict.get(c, -1) != -1, lofd)
            #dictionaires without c
            for dict in tokeep:
                dict[c] = 1
            lofd = tokeep
            if throwOut:
                ret = max([max(list(map(lambda dict: len(dict.keys()),throwOut))), ret])       
            lofd.append({c : 1})
        if lofd:
            return max(ret, len(lofd[0].keys()))
        return ret

    def partition(pred, iterable):
        trues = []
        falses = []
        for item in iterable:
            if pred(item):
                trues.append(item)
            else:
                falses.append(item)
        return trues, falses

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring(" "))