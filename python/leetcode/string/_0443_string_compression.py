"""
_0443_string_compression

Takeaways:
- Better use for loop, if cases more than one
- Take care about last element

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def compress(self, chars: List[str]) -> int:

        prev = chars[0]
        count = 0
        low = 0

        for i in range(0, len(chars)+1):

            char = chars[i] if i < len(chars) else None
      
            if char == prev:
                count += 1
            else:
                chars[low] = prev
                low += 1
                prev = char

                if count > 1:
                    count_list = list(str(count))
                    for c in count_list:
                        chars[low] = c
                        low += 1

                count = 1

        return low

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # chars = ["a","a","b","b","c","c","c"]
    # chars = ["a","a","b","b","c","c","c","b"]
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # chars = ["a"]

    print(chars)
    result = solution.compress(chars)
    print(result, chars)