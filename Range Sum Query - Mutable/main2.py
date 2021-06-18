from typing import List

class NumArray:
    head = None

    def __init__(self, nums: List[int]):
        self.head = NumArray.balance(nums, 0, len(nums) - 1)

    def balance(nums: List[int], left: int, right: int):
        if left == right:
            return Node(nums[left], left, right, None, None)
        else:
            mid = (left + right) // 2
            lN = NumArray.balance(nums, left, mid)
            rN = NumArray.balance(nums, mid + 1, right)
            return Node(lN.value + rN.value, left, right, lN, rN)

    def update(self, index: int, val: int) -> None:
        NumArray.updateH(self.head, index, val)
    
    def updateH(node, index, val):
        if node.leftIndex == index and index == node.rightIndex:
            node.value = val
        else:
            if node.leftNode.rightIndex < index:
                newNum = NumArray.updateH(node.rightNode, index, val)
                node.value = newNum + node.leftNode.value
            else:
                newNum = NumArray.updateH(node.leftNode, index, val)
                node.value = newNum + node.rightNode.value
        return node.value

    def sumRange(self, left: int, right: int) -> int:
        return NumArray.sumN(self.head, left, right)

    def sumN(node, left, right):
        # print(left)
        # print(right)
        # print('start')
        if node.leftIndex == left and node.rightIndex == right:
            return node.value
        else:
            # print(node.leftNode.rightIndex)
            # print(node.rightNode.leftIndex)
            # print('else')
            if node.leftNode.rightIndex < left:
                return NumArray.sumN(node.rightNode, left, right)
            elif node.rightNode.leftIndex > right:
                return NumArray.sumN(node.leftNode, left, right)
            else:
                mid = (left + right) // 2
                return NumArray.sumN(node.leftNode, left, mid) + NumArray.sumN(node.rightNode, mid + 1, right)

class Node:
    def __init__(self, val, leftIndex, rightIndex, leftNode, rightNode):
        self.value = val
        self.leftIndex = leftIndex
        self.rightIndex = rightIndex
        self.leftNode = leftNode
        self.rightNode = rightNode

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3])
# obj = NumArray(nums)
obj.update(2,4)
param_2 = obj.sumRange(1,2)
print(obj.sumRange(0,1))
print(obj.head.value)
