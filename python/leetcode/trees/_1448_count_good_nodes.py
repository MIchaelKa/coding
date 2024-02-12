"""
_1448_count_good_nodes

Takeaways:

"""

from common.tree import *

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(log(n))
    """
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))
    
    def goodNodesHelper(self, node: TreeNode, value: int) -> int:

        if node is None:
            return 0
        
        next_val = max(node.val, value)
        
        left = self.goodNodesHelper(node.left, next_val)
        right = self.goodNodesHelper(node.right, next_val)

        addition = 1 if node.val >= value else 0

        return left + right + addition

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    array = [3,1,4,3,None,1,5]
    # array = [9,None,3,None,None,6,None]

    tree = init_tree_from_array_2(array)
    tree.show()

    result = solution.goodNodes(tree)
    print(result)