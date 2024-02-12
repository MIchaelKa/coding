"""
_0124_tree_max_sum_path

Takeaways:

#tree

"""

from common.tree import *

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float('-inf')
        _ = self.maxPathSumHelper(root)
        return self.max_path
    
    def maxPathSumHelper(self, node: Optional[TreeNode]) -> int:

        if not node:
            return float('-inf')
        
        left = self.maxPathSumHelper(node.left)
        right = self.maxPathSumHelper(node.right)

        node_sum = (left if left != float('-inf') else 0) + (right if right != float('-inf') else 0) + node.val

        max_lr = max(left, right)
        max_node_path = max(max_lr, node_sum, node.val)
        max_branch_path = max((max_lr if max_lr != float('-inf') else 0) + node.val, node.val)
    
        self.max_path = max(self.max_path, max_node_path, max_branch_path)

        # print(max_node_path)

        return max_branch_path

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # print(float('-inf') == float('-inf'))

    # array = [-10,9,20,None,None,15,7]
    # array = [3, 10,-5, -1,None,10,10, None,None,None,None,-2,-1,3,4, None,None,None,None,None,None,None,None,None,None,7,None]
    # array = [3, 10,-5, -1,None,10,10, None,None,None,None,-2,-1,3,4]
    # array = [2, -1, None]
    array = [1,-2,3]

    print(array)


    tree = init_tree_from_array_2(array)
    # print(list(tree))
    tree.show()

    result = solution.maxPathSum(tree)
    print(result)