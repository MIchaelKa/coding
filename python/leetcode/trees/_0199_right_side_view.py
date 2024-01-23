"""
_0199_right_side_view

Takeaways:
- We can insert and read from a list at the same time if iterating using range(len())

"""

from common.tree import *
from typing import List

from collections import deque

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(log(n))
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        result = []

        if root:
            queue.append(root)

        while queue:

            result.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

def run_tests(solution):
    print("test passed!")

def main():

    # test()
    # return

    solution = Solution()

    run_tests(solution)

    tree = init_tree_from_array([10,1,3,5,20,15,27,4,2])
    # tree = init_tree_from_array([10])
    # tree = init_tree_from_array([])
    # tree.show()

    result = solution.rightSideView(tree)
    print(result)


def test():
    nodes = [1,2,3]

    # for i in range(len(nodes)):
    #     nodes.append(3+i)
    #     print(nodes[i])

    for n in nodes:
        nodes.append(n+1)
        print(n)

    print(nodes)