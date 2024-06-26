"""
_0567_permutation_in_str

https://leetcode.com/problems/permutation-in-string/description/

Takeaways:

Solutions:
- Sliding windows + compare hash_map - O(26*n)

TODO:
- reimplement with O(26) memory dict(list)

"""

from collections import Counter

class Solution_1:
    """
        Solution.

        Complexity:
            time: O(n+m) ?
            memory: O(m)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter = {}
        for c in s1:
            counter[c] = counter.get(c, 0) + 1

        cur_counter = counter.copy()

        start = 0

        for i in range(len(s2)):

            if s2[i] not in cur_counter:

                if s2[i] in counter:
                    while s2[start] != s2[i] and start < i:
                        cur_counter[s2[start]] = cur_counter.get(s2[start], 0) + 1
                        start += 1
                    start += 1
                else:
                    cur_counter = counter.copy()
                    start = i+1

                continue

            cur_counter[s2[i]] -= 1
            if cur_counter[s2[i]] == 0:
                cur_counter.pop(s2[i])
            
            if len(cur_counter) == 0:
                return True

        return False

class Solution:
    """
        Re-implementation of Solution_1.

        Complexity:
            time: O(n)
            memory: O(m)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = Counter(s1)

        low = 0
        high = 0

        while high < len(s2):
            if s2[high] not in s1_counter:
                high += 1
                low = high
                s1_counter = Counter(s1)
                continue
            else:
                if s1_counter[s2[high]] > 0:
                    s1_counter[s2[high]] -= 1
                    high += 1
                else:
                    while s2[low] != s2[high]:
                        s1_counter[s2[low]] += 1
                        low += 1
                    low += 1
                    high += 1

            if high-low == len(s1):
                return True

        return False



def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s1 = "ab"
    s2 = "eidbaooo"

    s1 = "adccb"
    s2 = "adccdba"

    print(s1, s2)
    result = solution.checkInclusion(s1, s2)
    print(result)

if __name__ == '__main__':
    main()