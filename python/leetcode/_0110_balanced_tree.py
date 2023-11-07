'''
110. Balanced Binary Tree

_0110_balanced_tree

Tags:
#tree

'''

from common.tree import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    
        _, balanced = self.dfs(root)
        return balanced
    
    def dfs(self, root: Optional[TreeNode]) -> (int, bool):

        left_h, left_b = 0, True
        if root.left is not None:
            left_h, left_b  = self.dfs(root.left)

        if not left_b:
            return (-1, False)

        right_h, right_b = 0, True
        if root.right is not None:
            right_h, right_b  = self.dfs(root.right)

        if not right_b:
            return (-1, False)
        
        left_h += 1
        right_h += 1

        return max(left_h, right_h), abs(left_h-right_h) <= 1


def main():
    solution = Solution()

    tree = init_tree_from_array([3,1,20,15,70])
    tree.show()

    answer = solution.isBalanced(tree)
    print(answer)