"""
_0045_jump_game_2

#array, #dp

"""

from typing import List

class Solution_1:
    """
        Greedy 1.
    """
    def jump(self, nums: List[int]) -> int:

        max_index = nums[0]
        steps = 1

        for i in range(1, nums):
            if max_index >= len(nums)-1:
                return steps
            if max_index == i:
                steps += 1
            if i + nums[i] > max_index:
                max_index = i + nums[i]

        return 0
    
class Solution:
    """
        DP
        bottom-up

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def jump(self, nums: List[int]) -> int:

        dp = [len(nums)] * len(nums)
        dp[0] = 0

        for i in range(len(nums)-1):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                dp[j] = min(dp[j], dp[i]+1)
            
        return dp[-1]

def run_tests(solution):
    assert(solution.jump([2,3,1,1,4])==2)
    assert(solution.jump([2,1,2,3,4,1,1,1,4])==3)
    assert(solution.jump([2,1])==1)
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [2,3,1,1,4]

    print(nums)
    result = solution.jump(nums)
    print(result)