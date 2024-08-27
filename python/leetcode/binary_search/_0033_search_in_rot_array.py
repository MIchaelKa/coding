"""
_0033_search_in_rot_array

Takeaways:

"""

from typing import List

class Solution_1:
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

class Solution:
    """
        Solution.
        NW

        Complexity:
            time: O()
            memory: O()
    """
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[high] < nums[low]:
                if target > nums[mid]:
                    if target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
                
            else:
                # binary serach
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

        
        return -1

def run_tests(solution):

    nums = [4,5,6,7,0,1,2]
    target = 0
    assert(solution.search(nums, target)==4)

    nums = [4,5,6,7,0,1,2]
    target = 3
    assert(solution.search(nums, target)==-1)

    nums = [9,1]
    target = 9
    assert(solution.search(nums, target)==0)

    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [4,5,6,7,8,1,2,3]
    target = 8

    print(nums, target)
    result = solution.search(nums, target)
    print(result)

if __name__ == '__main__':
    main()