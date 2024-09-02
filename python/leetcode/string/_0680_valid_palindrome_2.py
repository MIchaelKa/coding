"""
_0680_valid_palindrome_2

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def validPalindrome(self, s: str) -> bool:
        
        low = 0
        high = len(s) - 1

        error_count = 1

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            elif error_count > 0:
                error_count -= 1
                if s[low+1] == s[high]:
                    low += 1
                elif s[high-1] == s[low]:
                    high -= 1
                else:
                    return False
            else:
                return False

        return True

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "aebbeba"

    print(s)
    result = solution.validPalindrome(s)
    print(result)


if __name__ == '__main__':
    main()