"""
_0076_min_win_substring
https://leetcode.com/problems/minimum-window-substring

Takeaways:

Related problems:
_0567_permutation_in_str

Tags:
#strings

"""

from typing import List

class Solution:
    """
        Solution. Brute.

        Complexity:
            time: O(n)
            memory: O(m)
    """
    def minWindow(self, s: str, t: str) -> str:

        counter = {}
        for c in t:
            counter[c] = counter.get(c, 0) + 1

        cur_counter = counter.copy()
        add_counter = {}

        low = None
        min_substr = ""

        for high in range(len(s)):

            if low is None:
                if s[high] in counter:
                    low = high
                else:
                    continue

            if s[high] in counter:
                if s[high] in cur_counter:
                    cur_counter[s[high]] -= 1
                    if cur_counter[s[high]] == 0:
                        cur_counter.pop(s[high])
                else:
                    if s[high] == s[low]:
                        low += 1
                        while  s[low] in add_counter or (s[low] not in counter and low < high):
                            if s[low] in counter:
                                add_counter[s[low]] -= 1
                                if add_counter[s[low]] == 0:
                                    add_counter.pop(s[low])
                            low += 1
                    else:
                        add_counter[s[high]] = add_counter.get(s[high], 0) + 1


            if len(cur_counter) == 0 and (high-low+1 < len(min_substr) or len(min_substr) == 0):
                min_substr = s[low:high+1]

        return min_substr

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # s = "CBEDABC"
    # t = "ABC"

    s = "ADOBECODEBANC"
    t = "ABC"

    # s = "ab"
    # t = "b"

    print(s, t)
    result = solution.minWindow(s, t)
    print(result)