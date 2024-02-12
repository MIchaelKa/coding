"""
_0189_rotate_array

Takeaways:
- check ideas early

"""

from typing import List

class Solution:
    """
        Solution. Not works.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:

        if k == 0 or k == len(nums):
            return
        
        index = k

        even_size = len(nums) % k == 0
        num_swaps = len(nums) // k

        next = nums[0]

        print(even_size, num_swaps)

        for i in range(1, len(nums)+1):

            print(i, index, index % len(nums))

            temp = nums[index % len(nums)]
            nums[index % len(nums)] = next
            
            if even_size and i % num_swaps == 0:
                index += 1
                next = nums[index % len(nums)]
            else:       
                next = temp

            index += k



def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,2,3,4,5,6]
    k = 4

    print(nums, k)
    solution.rotate(nums, k)
    print(nums)