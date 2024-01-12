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
        self.k = k
        self.heap = heapq.nlargest(k, nums)

        # TODO: do we need heapify before call nlargest?
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)

        res = heapq.nlargest(self.k, self.heap)
        return res[-1]
            
        

def test_1():
    solution = KthLargest(3, [4,5,8,2])

    result = solution.add(3)
    print(result)

    result = solution.add(5)
    print(result)

def test_2():
    solution = KthLargest(1, [])

    result = solution.add(-3)
    print(result)

    result = solution.add(-2)
    print(result)

    result = solution.add(-4)
    print(result)


def main():
    test_1()
    
