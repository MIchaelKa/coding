"""
_0034_find_first_and_last

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums)-1
        mid = None

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if mid is None or nums[mid] != target:
            return [-1, -1]

        if nums[low] == target:
            high_2 = low
        else:
            high_2 = mid
            while high_2 - low > 1:
                mid_2 = (low + high_2) // 2
                if nums[mid_2] == target:
                    high_2 = mid_2
                else:
                    low = mid_2

        if nums[high] == target:
            low_2 = high
        else:
            low_2 = mid
            while high - low_2 > 1:
                mid_2 = (low_2 + high) // 2
                if nums[mid_2] == target:
                    low_2 = mid_2
                else:
                    high = mid_2
        
        return [high_2, low_2]

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [5,7,7,8,8,10]
    target = 8

    nums = [2,2]
    target = 2


    nums = [5,7,7,8,8,10]
    target = 6

    print(nums, target)
    result = solution.searchRange(nums, target)
    print(result)


if __name__ == '__main__':
    main()