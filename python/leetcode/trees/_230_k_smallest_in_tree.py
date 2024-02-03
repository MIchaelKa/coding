"""
_230_k_smallest_in_tree

Takeaways:
- be careful when use None for int

TODO: implement w/o recursion with stack/queue

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.kthSmallestHelper(root)
    
    def kthSmallestHelper(self, node: Optional[TreeNode]) -> int:

        if node is None:
            return None
        
        left = self.kthSmallestHelper(node.left)
        if left is not None:
            return left

        self.k -= 1
        if self.k == 0:
            return node.val
        
        right = self.kthSmallestHelper(node.right)
        if right is not None:
            return right
        
        return None


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    k = 3
    tree = init_tree_from_array([8,1,5,2,0,10])

    k = 3
    tree = init_tree_from_array([5,6,3,2,4,1])


    tree.show()
    result = solution.kthSmallest(tree, k)
    print(result)