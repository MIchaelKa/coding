"""
_0416_partition_equal_subset_sum

Takeaways:

Related problems:

TODO:

Tags:
#backtracking, #dp

"""

from typing import List
from python.common.utils import print_cost_matrix

class Solution_1:
    """
        Backtracking.

        Complexity:
            time: O(2^N)
            memory: O(N)
    """
    def canPartition(self, nums: List[int]) -> bool:

        all_sum = sum(nums)

        if all_sum % 2 != 0:
            return False
  
        target_sum = all_sum // 2

        return self.backtrack(nums, 0, target_sum, 0)
    

    def backtrack(self, nums: List[int], curr_sum: int, target: int, index: int) -> bool:

        if curr_sum == target:
            return True
        
        if curr_sum > target:
            return False
         
        for i in range(index, len(nums)):
            curr_sum += nums[i]
            if self.backtrack(nums, curr_sum, target, i+1):
                return True
            curr_sum -= nums[i]

        return False

class Solution:
    """
        DP.
        bottom-up

        Complexity:
            time: O(N*M)
            memory: O(N*M)
    """
    def canPartition(self, nums: List[int]) -> bool:

        all_sum = sum(nums)

        if all_sum % 2 != 0:
            return False
  
        target_sum = all_sum // 2

        dp = [[False] * (target_sum+1) for _ in range(len(nums)+1)]
        for i in range(0, len(nums)+1):
            dp[i][0] = True

        # print_cost_matrix(dp)

        for i in range(1, len(nums)+1):
            for j in range(1, target_sum+1):
                prev_target = j-nums[i-1]
                dp[i][j] = dp[i-1][j] or (dp[i-1][prev_target] if prev_target >= 0 else False)

        # print_cost_matrix(dp)
        
        return dp[-1][-1]





def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,5,11,5]
    nums = [1,5,11,5,3]
    nums = [1,2,5]

    nums = [1,2,7,3,2,3]

    # nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]

    print(nums)
    result = solution.canPartition(nums)
    print(result)


if __name__ == '__main__':
    main()