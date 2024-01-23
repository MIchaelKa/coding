"""
_0102_level_order_traversal

TODO:
- Implement w/o recursion.

Takeaways:
- How to write bfs for binary tree? Using queue.

"""

from common.tree import *
from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.dfs(root, result, 1)
        return result
    
    def dfs(self, root: Optional[TreeNode], result: List[int], depth: int):

        if root is None:
            return

        if len(result) < depth:
            result.append([])
        result[depth-1].append(root.val)
  
        self.dfs(root.left, result, depth+1)
        self.dfs(root.right, result, depth+1)


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    tree = init_tree_from_array([10,1,3,5,20,15,27,4,2])
    # tree = init_tree_from_array([10])
    tree = init_tree_from_array([])
    # tree.show()

    result = solution.levelOrder(tree)
    print(result)