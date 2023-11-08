'''
235. Lowest Common Ancestor of a Binary Search Tree

_0235_lca

Tags:
#tree

'''

from common.tree import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        node, _, _ = self.dfs(root, p, q)
        return node
    
    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> ('TreeNode', bool, bool):
        '''
        Assume p.val > q.val
        '''

        if root is None:
            return None, False, False

        p_found = root.val == p.val
        q_found = root.val == q.val

        if not p_found:
            left = self.dfs(root.left, p, q)
            if left[0] is not None:
                return left[0], True, True
            p_found = p_found or left[1]
            q_found = q_found or left[2]

        if not q_found:
            right = self.dfs(root.right, p, q)
            if right[0] is not None:
                return right[0], True, True
            p_found = p_found or right[1]
            q_found = q_found or right[2]

        # print(root.val, p_found, q_found)

        node = root if p_found and q_found else None

        return node, p_found, q_found
    
def run_tests(solution):

    tree = init_tree_from_array([6,2,8,0,4,7,9,3,5])
    p = tree.left
    q = tree.right.left
    assert(solution.lowestCommonAncestor(tree, p, q).val==6)

    tree = init_tree_from_array([6,2,8,0,4,7,9,3,5])
    p = tree.left.left
    q = tree.left.right.right
    assert(solution.lowestCommonAncestor(tree, p, q).val==2)

    print("test passed!")

def main():
    solution = Solution()

    run_tests(solution)

    tree = init_tree_from_array([2,1])
    tree.show()

    p = tree
    q = tree.left
    print(p.val, q.val)

    answer = solution.lowestCommonAncestor(tree, p, q)
    print(answer.val if answer else "None")