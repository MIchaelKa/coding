"""
_0763_partition_labels
https://leetcode.com/problems/partition-labels/description/

Takeaways:
- sometimes optimal solution is much more easy to code (see leetcode submissions)

Tags:
#string

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def partitionLabels(self, s: str) -> List[int]:

        last_idx = { c:i for i,c in enumerate(s) }

        low = 0
        high = 0
        result = []

        for i in range(len(s)):
            high = max(high, last_idx[s[i]])
            if i == high:
                result.append(high-low+1)
                low = high+1

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "ababcbacadefegdehijhklij"

    print(s)
    result = solution.partitionLabels(s)
    print(result)


if __name__ == '__main__':
    main()