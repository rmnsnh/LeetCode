from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        lofd = []
        for c in s:
            #add to each dictionary if not there, if it is, remove that instance
            for dict in lofd:
                # print(dict)
                if c in dict:
                    #set max length if more
                    l = len(dict.keys())
                    if ret < l:
                        ret = l
                    #remove
                    lofd.remove(dict)
                    # print(c)
                    # print("repeat")
                    # print(len(dict.keys()))
                else:
                    dict[c] = 1
            #create a dictionary with this element and add it to array
            lofd.append({c : 1})
        print([len(x.keys()) for x in lofd])
        print(ret)
        # print(newlist)
        # print(list(map(lambda dict: len(dict.keys()),lofd)))
        return 0
        # return max(ret, max(lofd, key=lambda dict: len(dict.keys())))

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring(" "))