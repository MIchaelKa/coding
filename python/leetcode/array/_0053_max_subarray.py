"""
_0053_max_subarray

#array

"""

from typing import List

class Solution_1:
    """
        Solution 1
        divide and conquer

        Takeaways:
        - Try do not make complex base cases for n>1

    """
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums)-1)
    
    def maxSubArrayHelper(self, nums: List[int], low: int, high: int) -> int:

        if high==low:
            return nums[low]
                    
        mid = (high+low) // 2
        left = self.maxSubArrayHelper(nums, low, mid)
        right = self.maxSubArrayHelper(nums, mid+1, high)
        cross = self.maxCrossingSubArray(nums, low, mid, high)

        return max(left, right, cross)

    def maxCrossingSubArray(self, nums: List[int], low: int, mid: int, high: int) -> int:

        max_left_sum = nums[mid]
        curr_sum = max_left_sum

        for i in range(mid-1, low-1, -1):
            curr_sum += nums[i]
            if curr_sum > max_left_sum:
                max_left_sum = curr_sum

        max_right_sum = nums[mid+1]
        curr_sum = max_right_sum

        for i in range(mid+2, high+1):
            curr_sum += nums[i]
            if curr_sum > max_right_sum:
                max_right_sum = curr_sum

        return max_left_sum + max_right_sum
        
class Solution:
    """
        Greedy

        Not works.
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

    solution = Solution_1()

    run_tests(solution)

    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [8,-19,5,-4,20]

    print(nums)
    result = solution.maxSubArray(nums)
    print(result)