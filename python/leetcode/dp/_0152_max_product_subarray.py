"""
_0152_max_product_subarray

Takeaways:

TODO:
- implement with two DP arrays

Tags:
#dp

"""

from typing import List

class Solution:
    """
        DP? + division.
        Not works. TLE.

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def maxProduct(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i-1] * nums[i] if dp[i-1] != 0 else nums[i]
            if dp[i] > max_prod:
                max_prod = dp[i]

        # print(dp)

        i = 0
        while  i < len(nums):

            while i < len(nums)-1 and nums[i] == 0:
                i += 1

            j = i+1
            while j < len(nums) and nums[j] != 0:
                dp[j] = dp[j] // nums[i]
                if dp[j] > max_prod:
                    max_prod = dp[j]
                j += 1
            
            i += 1

        return max_prod
    
class Solution:
    """
        DP.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def maxProduct(self, nums: List[int]) -> int:

        # TBD
        return 0

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    # nums = [5,0,8,-2,-1]
    # nums = [3,-1,4]
    nums = [0,-3,1,1]

    print(nums)
    result = solution.maxProduct(nums)
    print(result)

if __name__ == '__main__':
    main()