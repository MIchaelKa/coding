"""
[leetcode] 300. Longest Increasing Subsequence
LIS

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is an array that can be derived from another array by deleting some or
no elements without changing the order of the remaining elements.
"""

from typing import List

class Solution:
    """
    DP - ?

    Complexity:
        time : O(n^2)
        memory : O(n)
    """
    def __init__(self):
        self.verbose = False

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        table = [-1] * len(nums)
        max_lis_len = 1

        for i in range(0, len(nums)):
            table[i] = 1     
            max_subs_len = 0
            for j in range(i):
                if nums[j] < nums[i] and table[j] > max_subs_len:
                    max_subs_len = table[j]
                    table[i] = table[j]+1
                    if table[i] > max_lis_len:
                        max_lis_len = table[i]
        if self.verbose:
            print(table)
        return max_lis_len

def run_tests(solution):

    nums = [10,9,2,5,3,7,101,18]
    result = solution.lengthOfLIS(nums)
    assert(result == 4)

    nums = [10,9,2,5,3,7,101,18,6]
    result = solution.lengthOfLIS(nums)
    assert(result == 4)

    nums = [7,7,7,7,7]
    result = solution.lengthOfLIS(nums)
    assert(result == 1)

    print("Tests passed!")


if __name__ == '__main__':

    solution = Solution()
    run_tests(solution)

    solution.verbose = True
    
    nums = [2,4,3,5,1,7,6,9,8]
    result = solution.lengthOfLIS(nums)
    print(result)