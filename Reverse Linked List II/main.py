from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        this = head
        prev = None
        prevSecond = None
        isSecond = False
        while this is not None:
            next = this.next
            left -= 1
            right -= 1
            if left == 0:
                isSecond = True
            if right == 0:

                isSecond = False
            
            if not isSecond:
                this.next = prev
                prev = this
                this = next
            else:
                this.next = prevSecond
                prevSecond = this
                this = next

            # updateList = None
            # if isSecond:
            #     updateList = firstL
            # else:
            #     updateList = secondL

            # check if 
            # link 1 to end of two
        return prev

s = Solution()
print(s.reverseBetween("abcde", ["a","bb","acd","ace"]))
# print(s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))