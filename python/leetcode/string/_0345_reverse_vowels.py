"""
_0345_reverse_vowels

Takeaways:
- create set from a string -> set('AEIOUaeiou')

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1) ? or O(n)
    """
    def reverseVowels(self, s: str) -> str:
        
        low = 0
        high = len(s)-1

        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)

        while low < high:
            if s[low].lower() not in vowels:
                low += 1
                continue
            if s[high].lower() not in vowels:
                high -= 1
                continue

            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return ''.join(s)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "leetcode"

    print(s)
    result = solution.reverseVowels(s)
    print(result)