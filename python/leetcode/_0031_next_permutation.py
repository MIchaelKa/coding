"""
_0031_next_permutation

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Assume x is in [0,n] and every x in distinct.
        NW.

        Complexity:
            time: O()
            memory: O()
    """

    def swap(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    return j

        return -1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = self.swap(nums)

        if pivot < 0:
            low = 0
            high = len(nums)-1
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        hashmap = { i+1:1 for i in range(len(nums)) }
        
        for i in range(pivot+1):
            hashmap.pop(nums[i])

        res = list(hashmap.keys())
        for i in range(len(res)):
            nums[pivot+1+i] = res[i]
     

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [3,2,4,1]
    nums = [5,4,3,2,1]

    print(nums)
    solution.nextPermutation(nums)
    print(nums)


if __name__ == '__main__':
    main()