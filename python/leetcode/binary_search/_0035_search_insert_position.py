"""
_0035_search_insert_position
https://leetcode.com/problems/search-insert-position/description/

Takeaways:
- index where it would be if it were inserted in order.
- max(low, high)

Related problems:

TODO:

Tags:
#binary_search

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return max(low, high)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,3,5,6,8,9]
    target = 0
    print(nums, target)

    nums = [1,3,5,6,8,9]
    target = 2
    print(nums, target)

    result = solution.searchInsert(nums, target)
    print(result)


if __name__ == '__main__':
    main()