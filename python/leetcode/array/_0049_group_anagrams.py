"""
_0049_group_anagrams

Takeaways:
- python list as dict key (for optimal solution)

#array

"""

from typing import List
from collections import defaultdict

class Solution_1:
    """
        Naive solution with sorted.

        Complexity:
            time: O(m*n*log(n))
            memory:
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            dict["".join(sorted(s))].append(s)
        return list(dict.values())
    
class Solution_2:
    """
        TODO: more optimal with O(m*n)
    """

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution_1()

    run_tests(solution)

    strs = ["eat","tea","tan","ate","nat","bat"]

    print(strs)
    result = solution.groupAnagrams(strs)
    print(result)