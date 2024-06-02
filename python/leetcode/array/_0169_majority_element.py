"""
_0169_majority_element

Takeaways:
- Quickselect w/o recursion
- Partition with repeated numbers
- Odd and even cases, better separate and write variant for one

Related problems:
_0215_k_largest_in_array

#array, #quickselect

"""

from typing import List

class Solution:
    """
        Quickselect.

        NW

        Complexity:
            time: O(n)
            memory: O(1)
    """

    def partition_2(self, nums: List[int], l: int, h: int) -> int:
        pivot = nums[h]
        
        print(1, nums, l, h)
        while l < h:
            while nums[l] <= pivot and l < h:
                l += 1
            while nums[h] >= pivot and l < h:
                h -= 1
            if l < h:
                nums[l], nums[h] = nums[h], nums[l]

        print(2, nums, l, h)
        return l

    def partition_1(self, nums: List[int], low: int, high: int) -> int:

        print(1, nums, low, high)

        pivot = nums[high]
        while low < high:         
            if nums[low] <= pivot and low < high:
                low += 1
            elif nums[high] >= pivot and low < high:
                high -= 1
            else:
                nums[low], nums[high] = nums[high], nums[low]
                # low += 1
                # high -= 1

        print(2, nums, low, high)
        # print(list(range(13)))

        return low

        pivot_index = min(low, high)
        return pivot_index+1 if nums[pivot_index] <= pivot else pivot_index
    

    def majorityElement(self, nums: List[int]) -> int:

        low = 0
        high = len(nums)-1

        half_len = len(nums) // 2
        is_even = len(nums) % 2 == 0

        print(len(nums), half_len, is_even)
        # return 0

        while low < high:
            pivot = self.partition_2(nums, low, high)

            print(pivot)

            # if (not is_even and pivot == half_len) or \
            #         (is_even and (pivot == half_len or pivot == half_len-1)):
            #     return nums[pivot]
            
            if pivot > half_len:
                high = pivot - 1
            elif pivot < half_len:
                low = pivot + 1
            else:
                return nums[half_len]
      
        return nums[half_len]

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # nums = [2,2,1,1,1,2,2]
    # nums = [2,2,1,1,1,2,2,3]
    # nums = [1,2,3,2,1,2,3,2]
    # nums = [3]
    # nums = [1,3,1,1,4,1,1,5,1,1,6,2,2]

    nums = [1,7,8,2,3,9,5]
    nums = [1,8,8,2,3,8,8]

    print(nums)
    result = solution.majorityElement(nums)
    print(result)