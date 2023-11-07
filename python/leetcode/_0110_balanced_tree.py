'''
110. Balanced Binary Tree

_0110_balanced_tree

Notes:
Think about implementation of iterative solution.

Tags:
#tree

'''

from common.tree import *

class Solution_1:
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
    
class Solution_2:
    """
    Solution_2
    Less code.
    Is it slower than Solution_1?
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    
        _, balanced = self.dfs(root)
        return balanced
    
    def dfs(self, root: Optional[TreeNode]) -> (int, bool):     
        if root is None:
            return 0, True
            
        left, right = self.dfs(root.left), self.dfs(root.right)
        balanced = abs(left[0]-right[0]) <= 1 and left[1] and right[1]

        return max(left[0], right[0]) + 1, balanced
    
def run_tests(solution):

    tree = init_tree_from_array([3,1,20,15,70])
    assert(solution.isBalanced(tree)==True)

    tree = init_tree_from_array([1,3,20,15,70])
    assert(solution.isBalanced(tree)==False)

    print("tests passed.")

def main():
    solution = Solution_2()

    run_tests(solution)

    tree = init_tree_from_array([3,1,20,15,70])
    tree.show()

    answer = solution.isBalanced(tree)
    print(answer)