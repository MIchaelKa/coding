"""
[leetcode] 55. Jump Game

_0055_jump_game

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

#array

"""

from typing import List

class Solution:
    """
        Simple recursion w/o memoization
    """
    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpHelper(nums, 0)

    def canJumpHelper(self, nums: List[int], i: int) -> bool:
        if i >= len(nums)-1:
            return True
        for j in range(1, nums[i]+1):
            if self.canJumpHelper(nums, i+j):
                return True
        return False

class Solution2:
    """
        Recursion with memoization

        top-down or bottom up?
        top-down

    """
    def canJump(self, nums: List[int]) -> bool:
        self.cache = [False] * len(nums)
        return self.canJumpHelper(nums, 0)

    def canJumpHelper(self, nums: List[int], i: int) -> bool:
        if i >= len(nums)-1:
            return True
        if self.cache[i]:
            return False
        for j in range(1, nums[i]+1):
            if self.canJumpHelper(nums, i+j):
                return True
        self.cache[i] = True
        return False

class Solution3:
    """
        DP - bottom-up.
        (Still not optimal)
    """
    def canJump(self, nums: List[int]) -> bool:
        self.cache = [False] * len(nums)
        self.cache[0] = True
        
        for i, n in enumerate(nums):
            if not self.cache[i]:
                return False
            max_i = min(i+n+1, len(nums))
            for j in range(i+1, max_i):
                self.cache[j] = True

        return self.cache[-1]

class Solution4:
    """
        DP - ?
        Greedy - ?
        (Optimal)
    """
    def canJump(self, nums: List[int]) -> bool:
        most_reachable = 0
        for i, n in enumerate(nums):
            if i > most_reachable:
                return False
            if i+n > most_reachable:
                most_reachable = i+n
            if most_reachable >= len(nums)-1:
                return True

def run_tests(solution):

    nums = [2,3,1,1,4]
    result = solution.canJump(nums)
    assert(result==True)
    
    nums = [3,2,1,0,4]
    result = solution.canJump(nums)
    assert(result==False)

    print("Tests passed!")

if __name__ == '__main__':

    solution = Solution4()

    run_tests(solution)

    nums = [2,3,1,1,4]
    result = solution.canJump(nums)
    print(result)