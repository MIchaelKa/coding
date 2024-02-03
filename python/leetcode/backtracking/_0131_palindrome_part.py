"""
_0131_palindrome_part

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def partition(self, s: str) -> List[List[str]]:

        self.results = []
        indexes = [0]

        self.backtrack(0, s, indexes)

        return self.results
    
    def backtrack(self, low: int, s: str, indexes: List[int]):

        if low == len(s):
            palindroms = []
            low = 0
            for i in range(1, len(indexes)):
                palindroms.append(s[low:indexes[i]])
                low = indexes[i]
            self.results.append(palindroms)
            # self.results.append(indexes.copy())
            return
        
        for i in range(low+1, len(s)+1):
            if (self.is_palindrome(s[low:i])):
                # print(i)
                indexes.append(i)
                self.backtrack(i, s, indexes)
                indexes.pop(-1)

    def is_palindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "aabbbaaab"
    # s = "aab"

    # print(s[0:2], s[2:3])

    print(s)
    result = solution.partition(s)
    print(result)