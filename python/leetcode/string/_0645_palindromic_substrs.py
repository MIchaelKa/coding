"""
_0645_palindromic_substrs
https://leetcode.com/problems/palindromic-substrings/description/

Takeaways:

Related problems:
_0005_longest_palindromic_substr

#palindrom

"""

from common.utils import print_cost_matrix

class Solution_1:
    """
        DP.

        Complexity:
            time: O(n^2)
            memory: O(n^2)

        TODO: Fix memory usage from O(n^2) to O(n)
    """
    def countSubstrings(self, s: str) -> int:

        count = len(s)

        dp = [[False]*n for n in range(len(s),0,-1)]
        
        for i in range(len(dp)):
            dp[i][0] = True

        for i in range(len(dp)-1):
            if s[i] == s[i+1]:
                count += 1
                dp[i][1] = True

        for j in range(2, len(dp)):
            for i in range(0, len(dp)-j):
                # print(i,j,dp[i+1][j-2])
                dp[i][j] = dp[i+1][j-2] and s[i] == s[j+i]
                if dp[i][j]:
                    # print(i,j,s[i],s[j+i])
                    count += 1

        # print_cost_matrix(dp)
                
        return count
    

class Solution:
    """
        Expand from centers.

        Complexity:
            time: O(n^2)
            memory: O(1)

    """

    def expand(self, s: str, i: int, j: int):

        count = 0

        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                count += 1
            else:
                break
            i -= 1
            j += 1

        return count

    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):
            count += self.expand(s,i,i)
            # print(s[i], count)

        for i in range(len(s)-1):
            count += self.expand(s,i,i+1)
            # print(s[i], s[i+1], count)
     
        return count

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "abfabaa"
    # s = "aaaaa"

    print(s)
    result = solution.countSubstrings(s)
    print(result)