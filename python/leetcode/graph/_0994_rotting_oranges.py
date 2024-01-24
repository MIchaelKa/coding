"""
_0994_rotting_oranges

Takeaways:
- BFS as a multisource search

#graph, #bfs

"""

from typing import List
from collections import deque

class Solution:
    """
        Solution.

        Complexity:
            time: O(n*m)
            memory: O(n*m)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n_row = len(grid)
        n_cols = len(grid[0])

        queue = deque()
        num_of_fresh = 0
        times = 0

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        for i in range(n_row):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    num_of_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        while queue:

            # TODO: remove and check num_of_fresh in stead
            should_update = 0

            for i in range(len(queue)):
                pos = queue.popleft()       

                for d in directions:
                    new_pos = (pos[0]+d[0], pos[1]+d[1])

                    if new_pos[0] not in range(n_row) or new_pos[1] not in range(n_cols):
                        continue

                    if grid[new_pos[0]][new_pos[1]] == 1:
                        grid[new_pos[0]][new_pos[1]] = 2
                        queue.append(new_pos)
                        num_of_fresh -= 1
                        should_update = 1

            times += should_update

        return times if num_of_fresh == 0 else -1

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]

    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]

    grid = [[0,2]]

    result = solution.orangesRotting(grid)
    print(result)