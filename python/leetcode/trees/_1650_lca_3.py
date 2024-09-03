"""
_1650_lca_3
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii

Takeaways:

TODO:

Related problems:
Tags:

"""

from python.common.tree import *

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        pd = self.depth(p)
        qd = self.depth(q)

        diff = abs(pd - qd)

        print(diff, pd, qd)
            
        if pd > qd:
            for _ in range(diff):
                p = p.parent
        elif qd > pd:
            for _ in range(diff):
                q = q.parent

        print(p.val, q.val)

        return self.search(p, q)


    def search(self, p: 'Node', q: 'Node') -> 'Node':

        if not p.parent:
            return p
        
        if not q.parent:
            return q
        
        if p.val == q.val:
            return p

        if p.parent.val == q.parent.val:
            return p.parent
        
        return self.search(p.parent, q.parent)
        

    def depth(self, n: 'Node') -> int:
        if not n.parent:
            return 0    
        return 1 + self.depth(n.parent)
        


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    array = [3,5,1,6,2,0,8,None,None,7,4]
    # array = [1,2,None]

    tree = init_tree_from_array_2(array)
    tree.show()

    p = tree.left
    q = tree.left.right.right

    # p = tree
    # q = tree.left
    print(p.val, q.val)

    result = solution.lowestCommonAncestor(p, q)
    print(result.val)


if __name__ == '__main__':
    main()