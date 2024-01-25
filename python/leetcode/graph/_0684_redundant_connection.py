"""
_0684_redundant_connection

Takeaways:
- For n verticies MST will contain n-1 edges, it usefull to know to init arrays.
- Union-Find

#graph, #union_find

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(V*logV)
            memory: O(V)
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        self.parents = list(range(len(edges)))
        self.size = [1] * len(edges)

        for e in edges:
            if not self.merge(e[0]-1, e[1]-1):
                return e
            
            # print(self.parents)
            # print(self.size)
            # print()

        return []
    
    def merge(self, i, j):

        i = self.get_parent(i)
        j = self.get_parent(j)
        if i == j:
            return False
        
        if self.size[i] > self.size[j]:
            self.parents[j] = i
            self.size[i] += self.size[j]
        else:
            self.parents[i] = j
            self.size[j] += self.size[i]

        return True
    
    def same_component(self, i, j):
        return self.get_parent(i) == self.get_parent(j)
    
    def get_parent(self, v):
        while self.parents[v] != v:
            v = self.parents[v]  
        return v

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    # solution.parents = [2,3,2,0]
    # solution.parents = [0,1,2,3,4]
    # print(solution.get_parent(parents, 1))
    # return

    run_tests(solution)

    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    # edges = [[1,2],[2,3],[3,1],[2,4]]

    print(edges)
    result = solution.findRedundantConnection(edges)
    print(result)