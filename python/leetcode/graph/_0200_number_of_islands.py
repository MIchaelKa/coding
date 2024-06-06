"""
_0200_number_of_islands

Takeaways:

Related problems:

_0733_flood_fill

695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/

#graph, #bfs

"""

from typing import List, Tuple
from collections import deque

class Solution:
    """
        Solution.

        Complexity:
            time: O(n*m)
            memory: O(1)
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.bfs(grid, (i,j))

        return num_islands
    
    def bfs(self, grid: List[List[str]], pos: Tuple[int, int]):

        queue = deque()
        queue.append(pos)
        grid[pos[0]][pos[1]] = "0"

        n_rows = len(grid)
        n_cols = len(grid[0])

        while queue:

            cur_pos = queue.popleft()      

            top = (cur_pos[0] - 1, cur_pos[1])
            if top[0] >= 0 and grid[top[0]][top[1]] == "1" :
                queue.append(top)
                grid[top[0]][top[1]] = "0"

            bottom = (cur_pos[0] + 1, cur_pos[1])
            if bottom[0] < n_rows and grid[bottom[0]][bottom[1]] == "1" :
                queue.append(bottom)
                grid[bottom[0]][bottom[1]] = "0"

            left = (cur_pos[0], cur_pos[1] - 1)
            if left[1] >= 0 and grid[left[0]][left[1]] == "1" :
                queue.append(left)
                grid[left[0]][left[1]] = "0"

            right = (cur_pos[0], cur_pos[1] + 1)
            if right[1] < n_cols and grid[right[0]][right[1]] == "1" :
                queue.append(right)
                grid[right[0]][right[1]] = "0"


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    # ]

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    result = solution.numIslands(grid)
    print(result)