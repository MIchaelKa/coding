'''
[leetcode] 15. 3Sum

_0015_3_sum

Tags:
#array

'''

from typing import List
from common.utils import binary_search

class Solution_1:
    """
    Solution 1.

    Using recursion.
    See is_add_up_to_t.

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.threeSumHelper(nums, target=0, k=3)


    def threeSumHelper(self, nums: List[int], target: int, k: int) -> List[List[int]]:

        print(f'nums={nums}, target={target}, k={k}')

        if k == 1:
            index = binary_search(nums, target)
            # print(f'binary_search={nums[index] if index is not None else None}')
            return [[nums[index]]] if index is not None else []

        final_results = []
        current = None

        for i in range(len(nums)-1):
            if nums[i] == current:
                continue
            current = nums[i]

            if nums[i] > target:
                break
            
            new_target = target - nums[i]
            # print(f'num={nums[i]}')
            results = self.threeSumHelper(nums[i+1:], new_target, k-1)

            for result in results:
                final_results.append([nums[i]]+result)

        return final_results
    

class Solution_2:
    """
    Solution 2.

    Using twoSum

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # print(nums)

        final_results = []
        target = 0
        current = None

        for i in range(len(nums)-1):
            if nums[i] == current:
                continue
            current = nums[i]

            new_target = target - current
            low = i+1
            high = len(nums)-1

            # print(f'num={nums[i]}, new_target={new_target}')

            low_num = None
            high_num = None

            while low < high:

                # print(f'low={low}, high={high}')

                if nums[low] == low_num:
                    low += 1
                    continue

                if nums[high] == high_num:
                    high -= 1
                    continue

                guess = nums[low] + nums[high]
                if guess < new_target:
                    low += 1
                elif guess > new_target:
                    high -= 1
                else:
                    final_results.append([current, nums[low], nums[high]])
                    low_num = nums[low]
                    high_num = nums[high]
                    low += 1
                    high -= 1                 

        return final_results



def main():

    solution = Solution_2()

    # nums = [-1,0,1,2,-1,-4]
    # nums = [0,1,1]
    # nums = [0,0,0]
    # nums = [1,-1,-1,0]
    # nums = [-1,0,1,2,3,4,5,6,7]
    # nums = [-2,0,1,1,2,3,4,5,6,7]
    nums = [-2,0,0,2,2]
    answer = solution.threeSum(nums)

    print(answer)