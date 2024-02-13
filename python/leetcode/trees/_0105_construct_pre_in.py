"""
_0105_construct_pre_in

Takeaways:

"""

from typing import List, Optional
from common.tree import *

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder, inorder)
    
    def buildTreeHelper(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # print(preorder, inorder)

        if len(preorder) <= 0:
            return None
        
        val = preorder[0]
        node = TreeNode(val=val)

        if len(preorder) == 1:
            return node

        sep = None
        for i in range(len(inorder)):
            if inorder[i] == val:
                sep = i
                break

        # print(i, sep)

        node.left = self.buildTreeHelper(preorder[1:sep+1], inorder[0:sep])
        node.right = self.buildTreeHelper(preorder[sep+1:len(preorder)], inorder[sep+1:len(inorder)])

        return node


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    preorder = [3,9,1,20,15,7]
    inorder = [1,9,3,15,20,7]

    print(preorder, inorder)
    result = solution.buildTree(preorder, inorder)
    print(list(result))