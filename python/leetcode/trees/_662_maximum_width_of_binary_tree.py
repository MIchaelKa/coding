"""
_662_maximum_width_of_binary_tree
https://leetcode.com/problems/maximum-width-of-binary-tree/description/

Takeaways:
- (is not None) check for int 
- array for each level
- *2 for start index on the next level

Related problems:
_0199_right_side_view

TODO:
- make bfs solution work

Tags:
#tree

"""

from python.common.tree import *

class Solution_1:
    """
        DFS

        Complexity:
            time: O(n)
            memory: O(log(n))
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.intervals = [] 
        self.traverse(root, 0, 0)
        
        print(self.intervals)
        
        max_interval = 0
        for interval in self.intervals:
            max_interval = max(max_interval, interval[1]-interval[0])
            
        return max_interval+1
        
    def traverse(self, root: Optional[TreeNode], level: int, start_index: int):
        
        if not root:
            return
                        
        if root.left:
            self.check_interval(level, start_index)   
                
        if root.right:
            self.check_interval(level, start_index+1)
        
        # dfs
        self.traverse(root.left, level+1, start_index*2)
        self.traverse(root.right, level+1, start_index*2+2)
        
    def check_interval(self, level: int, index: int):
        
        if len(self.intervals) < level+1:
            self.intervals.append([None,None])
        
        if self.intervals[level][0] is not None:
            if index < self.intervals[level][0]:
                self.intervals[level][0] = index
        else:
            self.intervals[level][0] = index

        if self.intervals[level][1] is not None:
            if index > self.intervals[level][1]:
                self.intervals[level][1] = index
        else:
            self.intervals[level][1] = index

from collections import deque

class Solution_2:
    """
        BFS
        not works

        Complexity:
            time: O()
            memory: O()
    """
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque()

        if root:
            queue.append(root)


        while queue:

            low = None
            high = None


            for i in range(len(queue)):
                node = queue.popleft()

                if node is None:
                    continue

                if low is None:
                    low = i
                else:
                    high = i

                queue.append(node.left)
                queue.append(node.right)


            if low is None:
                continue

            if high is None:
                high = low

            width = high - low + 1

            print(width)

        return 0
    

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution_1()

    array = [1,3,2,5,3,None,9]
    # array = [1,3,2,5,None,None,9,6,None,None,None,None,None,7,None]

    tree = init_tree_from_array_2(array)
    tree.show()

    result = solution.widthOfBinaryTree(tree)
    print(result)


if __name__ == '__main__':
    main()