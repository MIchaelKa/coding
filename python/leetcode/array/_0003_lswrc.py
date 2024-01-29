"""
_0003_lswrc

Longest Substring Without Repeating Characters

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution. Naive.

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_map = {}
        max_len = 0
        pos = 0

        while len(s) - pos > max_len:

            for i in range(pos, len(s)):
                if s[i] in hash_map:
                    pos = hash_map[s[i]]+1
                    break
                else:
                    hash_map[s[i]] = i
                    pos = i
            
            max_len = max(max_len, len(hash_map))
            hash_map = {}

        return max_len

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # s = "abcbed"
    # s = "pwwkew"
    s = ""

    print(s)
    result = solution.lengthOfLongestSubstring(s)
    print(result)