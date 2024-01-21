"""
_0033_search_in_rot_array

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(log(n))
            memory: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1

        while l < h-1:
            mid = (l + h) // 2
            if nums[l] <= target and target <= nums[h]:
                if nums[mid] <= target:
                    l = mid
                else:
                    h = mid
            elif nums[l] <= target and target <= nums[mid]:
                h = mid
            elif nums[mid] <= target and target <= nums[h]:
                l = mid
            elif nums[mid] >= nums[l]:
                l = mid
            else:
                h = mid

        if nums[l] == target:
            return l
        elif nums[h] == target:
            return h
        else:
            return -1

def run_tests(solution):

    nums = [4,5,6,7,0,1,2]
    target = 0
    assert(solution.search(nums, target)==4)

    nums = [4,5,6,7,0,1,2]
    target = 3
    assert(solution.search(nums, target)==-1)

    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [9,1]
    target = 9

    print(nums, target)
    result = solution.search(nums, target)
    print(result)