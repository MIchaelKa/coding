"""
_0053_max_subarray

#array

"""

from typing import List

class Solution_1:
    """
        Solution 1
        divide and conquer

        Not works.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums)-1, 3)[0]
    
    def maxSubArrayHelper(self, nums: List[int], low: int, high: int, direction: int) -> (int, int, int):
        """
            Returns:
                - (int, int, int): tuple representing (max sum, left residual, right residual)
        """

        if high-low == 0:
            return nums[low], 0 , 0
        
        if high-low == 1:
            if nums[low] > 0 and nums[high] > 0:
                return nums[low]+nums[high], 0, 0
            elif nums[low] > 0:
                return nums[low], 0, nums[high]
            elif nums[high] > 0:
                return nums[high], nums[low], 0
            else:
                if nums[low] < nums[high]:
                    return nums[high], nums[low], 0
                else:
                    return nums[low], 0, nums[high]
                
        
        mid = (high+low) // 2
        left = self.maxSubArrayHelper(nums, low, mid, 1)
        right = self.maxSubArrayHelper(nums, mid+1, high, 2)

        merge_sum = left[0] + left[2] + right[1] + right[0]

        if direction==1:
            if merge_sum > right[0]:
                return merge_sum, left[1], right[2]
            else:
                return right[0], sum(left)+right[1], right[2]
        elif direction==2:
            if merge_sum > left[0]:
                return merge_sum, left[1], right[2]
            else:
                return left[0], left[1], sum(right)+left[2]    
        else:
            if merge_sum > left[0] and merge_sum > right[0]:
                return merge_sum, left[1], right[2]
            elif right[0] > left[0]:
                return right[0], sum(left)+right[1], right[2]
            else:
                return left[0], left[1], sum(right)+left[2]
        
class Solution:
    """
        Greedy
    """
    
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = nums[0]
        total_sum = nums[0]
        low = 0
        high = 1

        for i in range(1, len(nums)):

            if total_sum < 0 and nums[i] > cur_sum:
                print(total_sum, cur_sum, nums[i])
                low = high = i
                cur_sum = nums[i]
                total_sum = nums[i]
                continue

            total_sum += nums[i]

            if total_sum > cur_sum:
                cur_sum = total_sum
                high = i

        print(low, high)

        return cur_sum
    
def run_tests(solution):

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert(solution.maxSubArray(nums) == 6)

    nums = [-2,2,-1,5,-6,4,-5]
    assert(solution.maxSubArray(nums) == 6)

    nums = [5,4,-1,7,8]
    assert(solution.maxSubArray(nums) == 23)

    nums = [-3,-2,-1]
    assert(solution.maxSubArray(nums) == -1)

    nums = [-2,-3,-1]
    assert(solution.maxSubArray(nums) == -1)

    nums = [0,-3,1,1]
    assert(solution.maxSubArray(nums) == 2)

    nums = [-1,-2]
    assert(solution.maxSubArray(nums) == -1)

    print("test passed!")


def main():

    solution = Solution()

    run_tests(solution)

    nums = [8,-19,5,-4,20]

    print(nums)
    result = solution.maxSubArray(nums)
    print(result)