'''
[leetcode] 15. 3Sum

_0015_3_sum

Tags:
#array

'''

from typing import List
from common.utils import binary_search

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.threeSumHelper(nums, target=0, k=3)


    def threeSumHelper(self, nums: List[int], target: int, k: int) -> List[List[int]]:

        print(f'nums={nums}, target={target}, k={k}')

        if k == 1:
            index = binary_search(nums, target)
            return [[nums[index]]] if index is not None else None

        final_results = []
        current = None

        for i in range(len(nums)):

            if nums[i] == current:
                continue
            current = nums[i]
            
            new_target = target - nums[i]
            results = self.threeSumHelper(nums[i+1:], new_target, k-1)

            if results is None:
                continue

            for result in results:
                final_results.append([nums[i]]+result)

        return final_results



def main():

    solution = Solution()

    # nums = [-1,0,1,2,-1,-4]
    # nums = [0,1,1]
    nums = [0,0,0]
    answer = solution.threeSum(nums)

    print(answer)