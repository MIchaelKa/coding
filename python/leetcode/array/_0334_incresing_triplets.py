"""
_0334_incresing_triplets

Takeaways:
- if you need to find some finite sequence you can store in by element

"""

from typing import List

class Solution:
    """
        Solution. not optimal

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:

        cache = [1] * len(nums)
        
        for i in range(1, len(nums)):

            current_max = float('-inf')

            for j in range(1, i+1):
                if nums[i] >= nums[i-j]:

                    if nums[i] > nums[i-j]:
                        cache[i] = max(cache[i], cache[i-j]+1)
                    else: # ==
                        cache[i] = max(cache[i], cache[i-j])
                
                    if cache[i] == 3:
                        return True
                    
                    current_max = max(current_max, nums[i-j])         
                    if current_max >= nums[i]-1:
                        break

        return False
    

class Solution:
    """
        Linear.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_num = nums[0]
        mid_num = None

        for i in range(1, len(nums)):

            if nums[i] <= min_num:
                min_num = nums[i]
            elif mid_num is None or nums[i] < mid_num:
                mid_num = nums[i]

            if mid_num is not None and nums[i] > mid_num:
                return True

        return False

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # nums = [10,100,12,9,10,2,11,13]
    nums = [10,100,11,9,8,2,1,13]

    # nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,3,7]
    # nums = [1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

    print(nums)
    result = solution.increasingTriplet(nums)
    print(result)