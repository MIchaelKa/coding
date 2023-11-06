'''
_0543_tree_diameter
'''


from common.tree import *

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h, d = self.diameterOfBinaryTreeHelper(root)
        return d

    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> (int, int):

        left_h, left_d = 0, 0
        if root.left is not None:
            left_h, left_d = self.diameterOfBinaryTreeHelper(root.left)
            left_h += 1

        right_h, right_d = 0, 0
        if root.right is not None:
            right_h, right_d = self.diameterOfBinaryTreeHelper(root.right)
            right_h += 1
  
        h = max(left_h, right_h)
        d = max(left_d, right_d, left_h + right_h)

        return h, d
    

def main():
    solution = Solution()

    tree = init_tree_from_array([4,2,5,1,3])
    tree.show()

    d = solution.diameterOfBinaryTree(tree)
    print(d)