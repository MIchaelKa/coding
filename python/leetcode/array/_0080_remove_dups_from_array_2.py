"""
_0080_remove_dups_from_array_2
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Takeaways:

Related problems:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:

        current_pos = 1
        dup_count = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup_count += 1
            else:
                dup_count = 0

            if dup_count < 2:
                nums[current_pos] = nums[i]
                current_pos += 1

        return current_pos

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,1,1,2,2,3]
    nums = [1,1,1,1,2,2,2,3,4,5]

    print(nums)
    result = solution.removeDuplicates(nums)
    print(nums, result)