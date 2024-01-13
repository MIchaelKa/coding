"""
_0198_house_robber

#dp

"""

from typing import List

class Solution:

    # TODO: make this solution O(1) memory
    def rob(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
        


def main():
    solution = Solution()

    # nums = [2,7,9,3,1]
    # nums = [2,7,9,13,1]
    # nums = [1,9,1,1,9,1]
    # nums = [9,1]
    nums = [0]

    result = solution.rob(nums)
    print(result)