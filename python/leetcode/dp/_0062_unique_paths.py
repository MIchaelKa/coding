"""
[leetcode] 62. Unique Paths

#dp

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1]*n for _ in range(m)]

        # TODO: we can improve this solution saving only the last computed row

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print_dp_matrix(dp)

        return dp[-1][-1]

def print_dp_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        print("[", end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:3d}", end="")
        print("]")

if __name__ == '__main__':

    solution = Solution()

    result = solution.uniquePaths(7,3)
    print(result)

    result = solution.uniquePaths(1,3)
    print(result)