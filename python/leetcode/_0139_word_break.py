"""
_0139_word_break

Takeaways:
- Search in python set and list ~ takes the same time. Why?

TODO:
- Solution with trie

"""

from typing import List, Set

class Solution:
    """
        Solution.

        DP with memoization

        Complexity:
            time: O(n^2) - check all substrings
            memory: O(len(wordDict))
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        return self.wordBreakHelper(s, 0, set(wordDict), dp)
    
    def wordBreakHelper(self, s: str, i: int, wordDict: Set[str], dp: List[bool]) -> bool:

        if i == len(s):
            return True

        if dp[i]:
            return False
        
        for j in range(i+1, len(s)+1):
            key = s[i:j]
            if key in wordDict:
                if self.wordBreakHelper(s,j,wordDict,dp):
                    return True

        dp[i] = True
        return False

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "applepenapple"
    wordDict = ["apple","pen"]

    s = "acdead"
    wordDict = ["ac","acd","de","eadd"]

    print(s, wordDict)
    result = solution.wordBreak(s, wordDict)
    print(result)