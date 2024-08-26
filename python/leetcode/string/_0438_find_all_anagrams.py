"""
_0438_find_all_anagrams
https://leetcode.com/problems/find-all-anagrams-in-a-string/editorial/

Takeaways:

TODO:
- remove dict copy (curr_count = dict(counter))

Related problems:
- _0076_min_win_substring?
- _187_repeated_dna_sequences
    - https://leetcode.com/problems/repeated-dna-sequences/description/
    - - Rabin-Karp

Tags:
#strings

"""

from typing import List

from collections import Counter

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(m)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:

        counter = Counter(p)
        curr_count = dict(counter)

        if len(p) > len(s):
            return []
        
        low = 0
        high = 0

        result = []

        while high < len(s):
            
            if s[high] not in counter:
                high += 1
                low = high
                curr_count = dict(counter)
                continue

            if curr_count[s[high]] == 0:
                curr_count[s[low]] += 1
                low += 1
                continue

            curr_count[s[high]] -= 1  
            high += 1

            if high-low == len(p):
                result.append(low)
                curr_count[s[low]] += 1
                low += 1

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "cbaebabacd"
    p = "abc"

    s = "abcabc"
    p = "abc"

    s = "abacbabc"
    p = "abc"

    print(s,p)
    result = solution.findAnagrams(s,p)
    print(result)


if __name__ == '__main__':
    main()