from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = []
        for edge in edges:
            indexZeroExists = -1
            indexOneExists  = -1
            for i, graph in enumerate(graphs):
                if edge[0] in graph:
                    indexZeroExists = i
                if edge[1] in graph:
                    indexOneExists = i
            print(indexZeroExists)
            print(indexOneExists)
            if (indexZeroExists == -1) and (indexOneExists == -1):
                graphs.append({edge[0], edge[1]})
            elif (indexZeroExists == -1):
                graphs[indexOneExists].add(edge[0])
            elif (indexOneExists == -1):
                graphs[indexZeroExists].add(edge[1])
            elif indexZeroExists == indexOneExists:
                return edge
            else:
                graphs[indexZeroExists] = set.union(graphs[indexZeroExists], graphs[indexOneExists])
                graphs.pop(indexOneExists)


s = Solution()
print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))              #[2,3]
print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  #[1,4]
print(s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))  #[2,5]