"""
_0494_target_sum

Takeaways:

TODO:
- implement with backtracking and same cache size

"""

from typing import List
from collections import defaultdict

class Solution:
    """
        Solution.

        Complexity:
            time: O(n*?)
            memory: O()
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = [defaultdict(int) for _ in range(len(nums))]
        cache[0][nums[0]] += 1
        cache[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            for k, v in cache[i-1].items():
                cache[i][k+nums[i]] += v
                cache[i][k-nums[i]] += v

        if target in cache[-1]:
            return  cache[-1][target]

        return 0

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,1,1,1,1]
    target = 3

    nums = [1]
    target = 1

    nums = [0,0,0,0,0,0,0,0,1]
    target = 1

    print(nums, target)
    result = solution.findTargetSumWays(nums, target)
    print(result)