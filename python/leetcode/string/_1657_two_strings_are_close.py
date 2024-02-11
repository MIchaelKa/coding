"""
_1657_two_strings_are_close

Takeaways:
- We can compare sets and dicts with ==
- dict_keys vs. set

"""

from collections import Counter
from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)

        # TODO: set(word1) or we can save computations use and compare Counter(word1).keys()
        key_xor = len(set(count1.keys()) ^ set(count2.keys())) == 0

        if not key_xor:
            return False
        
        for i, j in zip(sorted(count1.values()), sorted(count2.values())):
            if i != j:
                return False

        return True

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    word1 = "cabbba"
    word2 = "abbccc"
    # word2 = "abbdcc"
    # word2 = "abbxxx"

    print(word1, word2)
    result = solution.closeStrings(word1, word2)
    print(result)