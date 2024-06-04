"""
_0054_spiral_matrix
https://leetcode.com/problems/spiral-matrix/description/

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.

        Not all corner cases works??

        Complexity:
            time:
            memory:
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        min_rc = min(rows, cols)

        num_spirals = int(min_rc / 2) + int(min_rc % 2)

        result = []

        # print(num_spirals)
        
        for s in range(0, num_spirals):

            low_r = s
            high_r = rows - s

            low_c = s
            high_c = cols - s

            # print(low_r, high_r)

            for i in range(low_c, high_c):
                result.append(matrix[low_r][i])

            for i in range(low_r+1, high_r-1):
                result.append(matrix[i][high_c-1])

            if high_r > low_r+1:
                for i in range(high_c-1, low_c-1, -1):
                    result.append(matrix[high_r-1][i])
 
            if high_c > low_c+1:
                for i in range(high_r-2, low_r, -1):
                    result.append(matrix[i][low_c])

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[7],[9],[6]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    result = solution.spiralOrder(matrix)
    print(result)