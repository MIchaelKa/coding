"""
_662_maximum_width_of_binary_tree

Takeaways:

Related problems:

Tags:
#tree

"""

from python.common.tree import *

class Solution:
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
            
        self.traverse(root.left, level+1, start_index)
        self.traverse(root.right, level+1, start_index+2)
        
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

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    array = [1,3,2,5,3,None,9]
    array = [1,3,2,5,None,None,9,6,None,None,None,None,None,7,None]

    tree = init_tree_from_array_2(array)
    tree.show()

    result = solution.widthOfBinaryTree(tree)
    print(result)


if __name__ == '__main__':
    main()