"""
_0703_k_largest_in_stream

#heap

"""

from typing import List
import heapq

class KthLargest:

    """
        Solution 1.
        Using python heapq
    """

    def __init__(self, k: int, nums: List[int]):
         
        self.nums = nums
        self.k = k

        # self.heap = [-x for x in nums]
        self.heap = nums
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:     
        heapq.heappush(self.heap, val)
        res = heapq.nlargest(self.k, self.heap)   
        return res[-1]


def main():
    solution = KthLargest(3, [4,5,8,2])

    result = solution.add(3)
    print(result)