"""
[leetcode] 1143. Longest Common Subsequence
LCS

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

from functools import lru_cache

class Solution:
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

def run_tests(solution):

    result = solution.longestCommonSubsequence("adbcde", "ace" )
    assert(result==3)

    result = solution.longestCommonSubsequence("afoshim", "bfishon")
    assert(result == 3)

    print("Tests passed!")


if __name__ == '__main__':

    solution = Solution()

    run_tests(solution)

    result = solution.longestCommonSubsequence("adbcde", "ace" )
    print(result)