"""
_0542_01_matrix

Takeaways:
- path in a matrix
- when you need bfs, not dfs
- multi-source bfs

TODO:
- dp approach

Related problems:
_0994_rotting_oranges

Tags:
#matrix, #bfs, #graph

"""

from typing import List
from python.common.utils import print_cost_matrix

class Solution_1:
    """
        DFS.
        NW.

        Complexity:
            time: O()
            memory: O()
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        result = [[None] * cols for _ in range(rows)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i: int, j: int):
            min_dist = rows + cols
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if new_i in range(rows) and new_j in range(cols):
                    if mat[i][j] == 0:
                        min_dist = 0
                        break
                    elif result[i][j] is not None:
                        min_dist = min(min_dist, result[i][j])
                    else:
                        result[i][j] = min_dist + 1
                        min_dist = min(min_dist, dfs(new_i, new_j))

            result[i][j] = min_dist + 1
            return result[i][j]
                        

        for i in range(rows):
            for j in range(cols):

                if result[i][j] is not None:
                    continue

                if mat[i][j] == 1:
                    dfs(i,j)
                else:
                    result[i][j] = 0

        return result

from collections import deque

class Solution:
    """
        BFS

        Complexity:
            time: O(n*m)
            memory: O(n*m)
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        result = [[0] * cols for _ in range(rows)]

        level = 0
        visited = set()  
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i, j))     

        while queue:

            for _ in range(len(queue)):

                i, j = queue.popleft()

                if  mat[i][j] == 1:
                    result[i][j] = level

                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if new_i in range(rows) and new_j in range(cols) and (new_i, new_j) not in visited:
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))

            level += 1

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    mat = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    result = solution.updateMatrix(mat)

    print_cost_matrix(mat)
    print()
    print_cost_matrix(result)


if __name__ == '__main__':
    main()