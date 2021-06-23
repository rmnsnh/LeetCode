from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head.next == None or left == right:
            return head
        this = head
        prev = None
        stash = None
        stashRev = None
        isReversed = False
        while this is not None:
            left -= 1
            right -= 1
            if left == 0:
                stash = prev
                stashRev = this
                isReversed = True
            if right == 0:
                if stash is not None:
                    stashRev.next = this.next
                    stash.next = this
                    this.next = prev
                    print(prev)
                    print(this)
                    print(head)
                    return head
                else:
                    print(prev)
                    print(this)
                    print(head)
                    stashRev.next = this.next
                    this.next = prev
                    return this

            if not isReversed:
                prev = this
                this = this.next
            else:
                next = this.next
                this.next = prev
                prev = this
                this = next

s = Solution()
print(s.reverseBetween("abcde", ["a","bb","acd","ace"]))