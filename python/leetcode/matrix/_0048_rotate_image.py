"""
_0048_rotate_image

https://leetcode.com/problems/rotate-image/description/

Takeaways:

Related problems:

Tags:
#matrix, #ml
"""

from typing import List
from python.common.utils import print_cost_matrix

class Solution:
    """
        Solution.

        Complexity:
            time: O(n^2)
            memory: O(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)
        num_of_circles = size // 2
        num_of_moves = size - 1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for c in range(num_of_circles):
            coords = [[c,c], [c, size-c-1], [size-c-1, size-c-1], [size-c-1, c]]

            for _ in range(num_of_moves):

                temp = matrix[coords[0][0]][coords[0][1]]

                for i in range(4):
                    j = i+1 if i < 3 else 0
                    c_to = coords[j]
                    v_to = matrix[c_to[0]][c_to[1]]
                    matrix[c_to[0]][c_to[1]] = temp
                    temp = v_to

                for coord, d in zip(coords, directions):
                    coord[0] += d[0]
                    coord[1] += d[1]

                # print()
                # print_cost_matrix(matrix)

            num_of_moves -= 2

        return None
        

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    matrix = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]

    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print_cost_matrix(matrix)
    solution.rotate(matrix)
    print()
    print_cost_matrix(matrix)


if __name__ == '__main__':
    main()