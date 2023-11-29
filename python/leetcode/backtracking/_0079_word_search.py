"""
_0079_word_search

Tags:
#backtracking

"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        cur_board = [[False] * cols for _ in range(rows)]

        def backtrack(pos, cur_board, last_cell):

            if pos == len(word):
                return True
            
            candidates = get_candidates(cur_board, last_cell)
            for c in candidates:
                if board[c[0]][c[1]] == word[pos]:
                    cur_board[c[0]][c[1]] = True
                    if backtrack(pos+1, cur_board, c):
                        return True
                    cur_board[c[0]][c[1]] = False

            return False


        def get_candidates(cur_board, last_cell):
            last_i, last_j = last_cell
            candidates = []

            if last_i+1 < rows and not cur_board[last_i+1][last_j]:
                candidates.append((last_i+1, last_j))

            if last_i-1 >= 0 and not cur_board[last_i-1][last_j]:
                candidates.append((last_i-1, last_j))

            if last_j+1 < cols and not cur_board[last_i][last_j+1]:
                candidates.append((last_i, last_j+1))

            if last_j-1 >= 0 and not cur_board[last_i][last_j-1]:
                candidates.append((last_i, last_j-1))

            return candidates

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    cur_board[i][j] = True
                    if backtrack(1, cur_board, (i,j)):
                        return True
                    cur_board[i][j] = False
    

        return False

def run_tests(solution):

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    result = solution.exist(board, word)
    assert(result)

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "SEE"
    result = solution.exist(board, word)
    assert(result)

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCB"
    result = solution.exist(board, word)
    assert(not result)

    print("tests passed!")


def main():
    solution = Solution()

    run_tests(solution)

    board = [["a","b"]]
    word = "ba"

    result = solution.exist(board, word)
    print(result)
