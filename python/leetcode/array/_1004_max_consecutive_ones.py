"""
_1004_max_consecutive_ones

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        low = 0
        high = 0
        max_len = 0
        edits = 0

        while high < len(nums):
      
            # TODO: remove while, one step at time
            while low <= high and edits > k :
                if nums[low] == 0:
                    edits -= 1
                low += 1

            if nums[high] == 0:
                edits += 1

            if edits <= k:
                max_len = max(max_len, high-low+1)

            high += 1

        return max_len

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    # nums = [0,0,0,1,1,0]
    k = 2

    print(nums, k)
    result = solution.longestOnes(nums, k)
    print(result)