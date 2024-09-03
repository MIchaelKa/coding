"""
_0215_k_largest_in_array

Takeaways:
- Quickselect

Related problems:
_0347_top_k_freq_elem

TODO:
- improve to O(n*log(k)) time complexity
- O(n*log(k)) is better than O(n + k*log(n)) ?

#array, #heap, #quickselect

"""

from typing import List

import heapq

class Solution_1:
    """
        Using heapq.

        Complexity:
            time: O(n + k*log(n))
            memory: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            _ = heapq.heappop(nums)
        return -heapq.heappop(nums)
        

class Solution:
    """
        Quickselect.

        Complexity:
            time:
                O(n^2) - worst case
                O(n) - average case
            memory: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestHelper(nums, k, 0, len(nums)-1)
    
    def findKthLargestHelper(self, nums: List[int], k: int, low: int, high: int) -> int:

        pivot = self.partition(nums, low, high)
        # print(pivot, nums)

        if pivot == len(nums)-k:
            return nums[pivot]
        elif pivot < len(nums)-k:
            return self.findKthLargestHelper(nums, k, pivot+1, high)
        else:
            return self.findKthLargestHelper(nums, k, low, pivot-1)
    
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        l, h = low, high

        while l < h:
            while nums[l] <= pivot and l < h:
                l += 1

            while nums[h] >= pivot and l < h:
                h -= 1

            if l < h:
                nums[l], nums[h] = nums[h], nums[l]
  
        # print(l, high)
        nums[l], nums[high] = nums[high], nums[l]
        return l

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [3,2,1,5,6,4]
    k = 2

    nums = [5,8,1,3,4,9,7,6]
    k = 2

    # nums = [3,2,1,5,5,6,4]
    # k = 2

    # nums = [99,99]
    # k = 1

    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4

    nums = [1,3,1,1,4,1,1,5,5,5,5,5,5,1,1,6,2,2]
    k=2

    print(nums, k)
    print(sorted(nums), k)
    result = solution.findKthLargest(nums, k)
    print(result)

if __name__ == '__main__':
    main()