'''
153. Find Minimum in Rotated Sorted Array

_0153_find_min_in_rot_array

Tags:
#array, #binary_search

'''

from typing import List

class Solution_1:
    def findMin(self, nums: List[int]) -> int:

        l, h = 0, len(nums)-1
        pivot = nums[h]

        while l < h-1:             
            i = (l + h) // 2

            if nums[i] > pivot:
                l = i
            else:
                h = i

            pivot = nums[i]

        return min(nums[l], nums[h])


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        h = len(nums)-1

        if nums[l] < nums[h]:
            return nums[l]

        while l < h-1:
            mid = (l + h) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                h = mid

        return nums[h]
        
def run_tests(solution):

    assert(solution.findMin([4,5,6,7,0,1,2]) == 0)
    assert(solution.findMin([2,3,4,5,6,7,8,0,1]) == 0)

    assert(solution.findMin([9,0,1,3,4,5,6,7,8]) == 0)
    assert(solution.findMin([8,9,0,1,3,4,5,6,7]) == 0)

    assert(solution.findMin([11,13,15,17]) == 11)

    assert(solution.findMin([4,5,1,2,3]) == 1)

    assert(solution.findMin([1]) == 1)

    print("test passed")

def main():

    solution = Solution()

    run_tests(solution)

    # nums = [2,3,4,5,6,7,8,0,1]
    nums = [9,0,1,3,4,5,6,7,8]

    print(nums)
    answer = solution.findMin(nums)
    print(answer)