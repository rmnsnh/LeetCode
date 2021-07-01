# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depth = 0
        breath = [[(root, 0)]]
        #(location, depth)
        locs = []
        while True:
            toCheck = breath[depth]
            if len(locs) != 2:
                for e in toCheck:
                    print(e)
                    if p == e[0]:
                        locs.append((e[1], depth))
                    if q == e[0]:
                        locs.append((e[1], depth))

            if len(locs) == 2:
                sameLevelPos = locs[1][0] // (2 ** (locs[1][1] - locs[0][1]))

                depthDif = 0
                while sameLevelPos // (2 ** depthDif) != locs[0][0] // (2 ** depthDif):
                    depthDif += 1
                
                for e in breath[locs[0][1] - depthDif]:
                    if e[1] == (sameLevelPos // (2 ** depthDif)):
                        return e[0]

            next = []
            for (e, pos) in toCheck:
                if e.left != None:
                    next.append((e.left, pos * 2))
                if e.right != None:
                    next.append((e.right, (pos * 2) + 1))
            breath.append(next)
            depth += 1