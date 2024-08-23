"""
_0416_partition_equal_subset_sum

Takeaways:

Related problems:

TODO:

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
    def canPartition(self, nums: List[int]) -> bool:

        all_sum = sum(nums)

        if all_sum % 2 != 0:
            return False
  
        target_sum = all_sum // 2

        return self.backtrack(nums, 0, target_sum, 0)
    

    def backtrack(self, nums: List[int], curr_sum: int, target: int, index: int) -> bool:

        if curr_sum == target:
            return True
        
        if curr_sum > target:
            return False
         
        for i in range(index, len(nums)):
            curr_sum += nums[i]
            if self.backtrack(nums, curr_sum, target, i+1):
                return True
            curr_sum -= nums[i]

        return False



def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,5,11,5]
    nums = [1,5,11,5,3]
    nums = [1,2,5]
    
    nums = [1,2,7,3,2,3]

    print(nums)
    result = solution.canPartition(nums)
    print(result)


if __name__ == '__main__':
    main()