"""
_0283_move_zeros

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
    def moveZeroes(self, nums: List[int]) -> None:

        zero_index = 0
        digit_index = 0

        while zero_index < len(nums) and nums[zero_index] != 0:
            zero_index += 1

        digit_index = zero_index+1
        
        while digit_index < len(nums):
            if nums[digit_index] != 0:
                nums[zero_index], nums[digit_index] = nums[digit_index], nums[zero_index]
                zero_index += 1
            digit_index += 1


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,3,0,0,4,5,0,0,0,6,7,8]
    # nums = [0,1,0,3,12]

    print(nums)
    solution.moveZeroes(nums)
    print(nums)