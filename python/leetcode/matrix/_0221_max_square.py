"""
_0221_max_square

Takeaways:

#matrix

"""

from typing import List

class Solution:
    """
        DP.

        TODO: Improve using one number in do matrix insted of (area, area_row, area_col)

        Complexity:
            time: O(n*m)
            memory: O(n*m)
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        area_max = 0

        areas = [[(0,0,0)]*cols for _ in range(rows)]

        areas[0][0] = (1,1,1) if matrix[0][0] == '1' else (0,0,0)
        area_max = 1 if matrix[0][0] == '1' else 0

        # (area, area_row, area_col)

        for i in range(1, cols):
            if matrix[0][i] == '1':
                areas[0][i] = (1, areas[0][i-1][1]+1, 1)
                area_max = 1

        for i in range(1, rows):
            if matrix[i][0] == '1':
                areas[i][0] = (1, 1, areas[i-1][0][2]+1)
                area_max = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    area = min(areas[i-1][j-1][0], areas[i-1][j][1], areas[i][j-1][2]) + 1
                    area_row = areas[i-1][j][1] + 1
                    area_col = areas[i][j-1][2] + 1
                    areas[i][j] = (area, area_row, area_col)

                    area_max = max(area_max, area)

        return area_max**2

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    matrix = [
        ["1","1","1","0","0"],
        ["1","1","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    result = solution.maximalSquare(matrix)
    print(result)