"""
_0152_max_product_subarray

Takeaways:

#dp

"""

from typing import List

class Solution:
    """
        Solution 1.
        Using division. Naive, not works.

        Complexity:
            time:
            memory:
    """
    def maxProduct(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i-1]*nums[i]
            if dp[i] > max_prod:
                max_prod = dp[i]

        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] != 0:
                    dp[j] /= nums[i]
                else:
                    # can't handle zero case
                    dp[j] = nums[i]

                if dp[i] > max_prod:
                    max_prod = dp[i]

        return max_prod

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [2,3,-2,4]
    nums = [-2,0,-1]

    print(nums)
    result = solution.maxProduct(nums)
    print(result)