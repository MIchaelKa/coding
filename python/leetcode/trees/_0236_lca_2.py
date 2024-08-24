"""
_0236_lca_2
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Takeaways:

TODO:

Related problems:
_0235_lca

Tags:
#tree

"""

from python.common.tree import *
from typing import Tuple

class Solution:
    """
        Solution.

        Complexity:
            time: O(N) # N - number of nodes
            memory: O(N) # for skewed tree - N is max amount of space utilized by recursion stack
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple['TreeNode', bool, bool]:

            if node is None:
                return None, False, False
            
            left, left_p, left_q = dfs(node.left, p, q)
            if left:
                return left, False, False
            
            right, right_p, right_q = dfs(node.right, p, q)
            if right:
                return right, False, False
            
            node_p = (left_p or right_p or node.val == p.val)
            node_q = (left_q or right_q or node.val == q.val)

            if node_p and node_q:
                return node, False, False
            
            return None, node_p, node_q
        
        node, _, _ = dfs(root, p, q)

        return node


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    tree = init_tree_from_array([6,2,8,0,4,7,9,3,5])
    p = tree.left
    q = tree.right.left

    tree.show()


    result = solution.lowestCommonAncestor(tree, p, q)
    print(result.val)


if __name__ == '__main__':
    main()