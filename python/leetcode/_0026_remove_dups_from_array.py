'''
[leetcode] 26. Remove Duplicates from Sorted Array
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j+1

if __name__ == '__main__':

    solution = Solution()

    # nums = [1,1,2]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [0,0,0]

    k = solution.removeDuplicates(nums)

    print(nums)
    print(k)