"""
_0074_search_matrix

Takeaways:

"""

from typing import List
from common.utils import print_cost_matrix

class Solution:
    """
        2x binary search.

        Complexity:
            time: O(log(m*n))
            memory: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows-1
        target_row = -1

        while low <= high:
            mid_row = (low + high) // 2
            if target < matrix[mid_row][0]:
                high = mid_row-1
            elif target > matrix[mid_row][cols-1]:
                low = mid_row+1
            else:
                target_row = mid_row
                break

        if target_row == -1:
            return False
        
        low = 0
        high = cols-1

        while low <= high:
            mid_col = (low + high) // 2
            if target < matrix[target_row][mid_col]:
                high = mid_col-1
            elif target > matrix[target_row][mid_col]:
                low = mid_col+1
            else:
                return True

        return False

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
    target = 23

    print(target)
    print_cost_matrix(matrix)
    
    result = solution.searchMatrix(matrix, target)
    print(result)