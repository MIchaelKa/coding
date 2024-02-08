"""
_0073_set_matrix_zero

Takeaways:
- save info in the data to make operation in-place

#matrix

"""

from typing import List

from common.utils import print_cost_matrix

class Solution:
    """
        Solution.

        Complexity:
            time: O(n^2)
            memory: O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zi, zj = None, None

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 and i != zi and j != zj:
                    if zi is None:
                        zi, zj = i, j
                        for k in range(rows):
                            if matrix[k][j] == 0:
                                matrix[k][j] = 1
                            else:
                                matrix[k][j] = 0
                        for k in range(cols):
                            if matrix[i][k] == 0:
                                matrix[i][k] = 1
                            else:
                                matrix[i][k] = 0
                        break
                    else:
                        matrix[zi][j] = 1
                        matrix[i][zj] = 1


        # print_cost_matrix(matrix)
        # print(zi, zj)

        if zi is not None:
            for k in range(cols):
                if matrix[zi][k] == 1:
                    for i in range(rows):
                        matrix[i][k] = 0

            for k in range(rows):
                if matrix[k][zj] == 1:
                    for i in range(cols):
                        matrix[k][i] = 0

        return

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # matrix = [
    #     [0,1,2,0],
    #     [3,4,5,2],
    #     [1,3,1,5]
    # ]

    # matrix = [
    #     [2,1,2,2,7],
    #     [3,0,5,0,9],
    #     [1,3,1,5,4]
    # ]

    matrix = [
        [0,0,0,5],
        [4,3,1,4],
        [0,1,1,4],
        [1,2,1,3],
        [0,0,1,1]
    ]

    print_cost_matrix(matrix)
    print()
    result = solution.setZeroes(matrix)
    print_cost_matrix(matrix)
    print(result)