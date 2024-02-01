"""
_1143_lcs

[leetcode] 1143. Longest Common Subsequence
LCS

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

#dp, #subsequence

"""

from functools import lru_cache

class Solution_1:
    """
        Simple recursion w/o memoization
        (using @lru_cache for built-in memoization functionality)
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceHelper(text1, text2, 0, 0)

    @lru_cache(None)
    def longestCommonSubsequenceHelper(self, text1: str, text2: str, i: int, j: int) -> int:
        if i == len(text1):
            return 0
        if j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            return 1 + self.longestCommonSubsequenceHelper(text1, text2, i+1, j+1)
        else:
            a = self.longestCommonSubsequenceHelper(text1, text2, i+1, j)
            b = self.longestCommonSubsequenceHelper(text1, text2, i, j+1)
            # c = self.longestCommonSubsequenceHelper(text1, text2, i+1, j+1) # do not need
            return max(a,b)
        
class Solution:
    """
        DP.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if (text1[i-1]==text2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]


def run_tests(solution):

    result = solution.longestCommonSubsequence("adbcde", "ace" )
    assert(result==3)

    result = solution.longestCommonSubsequence("afoshim", "bfishon")
    assert(result == 3)

    print("Tests passed!")


def main():

    solution = Solution()

    run_tests(solution)

    result = solution.longestCommonSubsequence("adbcde", "ace" )
    print(result)