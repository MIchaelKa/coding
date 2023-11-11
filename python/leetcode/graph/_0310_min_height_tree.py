"""
[leetcode] 310. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Tags:
#graph, #tree

"""

from typing import List

class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        self.graph = [[] for _ in range(n)]

        for x, y in edges:
            self.graph[x].append(y)
            self.graph[y].append(x)

        self.discovered = {}
        self.depth = {}

        #
        # Step 1. Calculate depth for all nodes starting from root
        #
        root = 0
        self.dfs(root)
        # print(self.depth)

        #
        # Step 2. Perform the search for good nodes
        #
        self.discovered = {}
        return self.search(root, -1)

    def search(self, v: int, depth: int) -> List[int]:

        self.discovered[v] = True

        if depth == 0:
            return [v]

        max_1 = max_2 = -1
        max_1_depth = max_2_depth = 0

        for child in self.graph[v]:
            if child in self.discovered:
                continue

            child_depth = self.depth[child]
            if child_depth > max_1_depth:
                if max_1_depth > max_2_depth:
                    max_2_depth = max_1_depth
                    max_2 = max_1
                max_1_depth = child_depth
                max_1 = child     
            elif child_depth > max_2_depth:
                max_2_depth = child_depth
                max_2 = child

        diff = max_1_depth - max_2_depth
        
        if diff == 0:
            return [v]
        else:

            if depth == -1:   
                depth = int(diff / 2) + int(diff % 2 != 0) # ceil
                self.more_than_one = (diff % 2 != 0)

            nodes = []
            
            nodes.extend(self.search(max_1, depth-1))

            if depth == 1 and (diff == 1 or self.more_than_one):
                nodes.append(v)

            return nodes
                

    def dfs(self, v: int):

        self.discovered[v] = True
        depth = 1

        for child in self.graph[v]:
            if child not in self.discovered:
                depth = max(depth, self.dfs(child)+1)

        self.depth[v] = depth

        return depth

def run_tests():
    solution = Solution()

    num_v = 1
    edges = []
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [0])
    
    num_v = 2
    edges = [[0,1]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [0,1])

    num_v = 4
    edges = [[1,0],[1,2],[1,3]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [1]) 

    num_v = 5
    edges = [[0,1],[0,2],[0,3],[3,4]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [0,3])

    num_v = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [3,4])

    num_v = 7
    edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [1,2])

    num_v = 8
    edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[5,7]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [3])

    num_v = 10
    edges = [[0,1],[0,2],[0,3],[2,4],[0,5],[5,6],[6,7],[2,8],[7,9]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [5])

    num_v = 11
    edges = [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]
    result = solution.findMinHeightTrees(num_v, edges)
    assert(sorted(result) == [5,6])

    print("test passed")


if __name__ == '__main__':

    run_tests()

    solution = Solution()

    num_v = 11
    edges = [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]
    result = solution.findMinHeightTrees(num_v, edges)
    print(result)

    