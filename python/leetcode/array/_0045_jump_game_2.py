"""
_0045_jump_game_2

#array, #dp, #greedy

"""

from typing import List
    
class Solution_1:
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
    

class Solution:
    """
        Greedy

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def jump(self, nums: List[int]) -> int:

        low_index = 1
        max_index = nums[0]
        next_max_index = max_index
        steps = 0

        while low_index < len(nums):
            
            for i in range(low_index, min(max_index+1, len(nums))):
                if i + nums[i] > next_max_index:
                    next_max_index = i + nums[i]

            low_index = max_index+1
            max_index = next_max_index    
            steps += 1
            
        return steps

def run_tests(solution):
    assert(solution.jump([2,3,1,1,4])==2)
    assert(solution.jump([2,1,2,3,4,1,1,1,4])==3)
    assert(solution.jump([2,1])==1)
    assert(solution.jump([0])==0)
    assert(solution.jump([1,2,3])==2)
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [2,1]

    print(nums)
    result = solution.jump(nums)
    print(result)