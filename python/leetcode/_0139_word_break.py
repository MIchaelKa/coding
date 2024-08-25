"""
_0139_word_break

Takeaways:
- Search in python set and list ~ takes the same time. Why?

TODO:
- Solution with trie

#dp

"""

from typing import List, Set

class Solution_1:
    """
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

class Solution_2:
    """
        DFS.

        Complexity:
            time: O(2^N)
            memory: O(N)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)

        def backtrack(i: int) -> bool:

            if i == len(s):
                return True

            for j in range(len(s)+1):
                word = s[i:j]
                if word in wordDict:
                    if backtrack(j):
                        return True


            return False

        return backtrack(0)
    

class Solution:
    """
        DP. bottom-up

        Complexity:
            time: O(N^2)
            memory: O(N)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        dp = [False] * len(s)

        for i in range(len(s)):
            j = i
            while j >= 0 and not dp[i]:
                dp[i] = (s[j:i+1] in wordDict) and (dp[j-1] if j > 0 else True)
                j -= 1

        return dp[-1]

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "applepenapple"
    wordDict = ["apple","pen"]

    # s = "acdead"
    # wordDict = ["ac","acd","de","eadd"]

    print(s, wordDict)
    result = solution.wordBreak(s, wordDict)
    print(result)

if __name__ == '__main__':
    main()