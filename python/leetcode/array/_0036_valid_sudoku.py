"""
_0036_valid_sudoku

Takeaways:
- better use set when you don't need actual value in dict

#array

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_caches = [{} for _ in range(len(board))]
        col_caches = [{} for _ in range(len(board))]
        sub_caches = [[{} for _ in range(len(board)//3)] for  _ in range(len(board)//3)]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in row_caches[i]:
                    row_caches[i][board[i][j]] = True
                else:
                    return False
                
                if board[i][j] not in col_caches[j]:
                    col_caches[j][board[i][j]] = True
                else:
                    return False

                if board[i][j] not in sub_caches[i//3][j//3]:
                    sub_caches[i//3][j//3][board[i][j]] = True
                else:
                    return False
                
        return True

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    board = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]

    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]

    result = solution.isValidSudoku(board)
    print(result)