"""
_0703_k_largest_in_stream

#heap

"""

from typing import List
import heapq

class KthLargest_1:

    """
        Solution 1.
        Using python heapq + nlargest
        
    """

    def __init__(self, k: int, nums: List[int]):       
        self.k = k
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            # Note:
            # since we started to use heappushpop and keep self.heep size
            # less or equal to k, we don't need nlargest anymore
            # see Solution 2
            heapq.heappushpop(self.heap, val)

        res = heapq.nlargest(self.k, self.heap)
        return res[-1]
    
class KthLargest_2:

    """
        Solution 2.
        Using python heapq
        
    """

    def __init__(self, k: int, nums: List[int]):       
        self.k = k
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)         

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)       
        else:
            heapq.heappushpop(self.heap, val) 
        return self.heap[0]
            
        

def test_1(class_name):
    solution = class_name(3, [4,5,8,2])

    result = solution.add(3)
    assert(result==4)

    result = solution.add(5)
    assert(result==5)

    result = solution.add(10)
    assert(result==5)

def test_2(class_name):
    solution = class_name(1, [])

    result = solution.add(-3)
    assert(result==-3)

    result = solution.add(-2)
    assert(result==-2)

    result = solution.add(-4)
    assert(result==-2)

def test_3(class_name):
    solution = class_name(2, [0])

    result = solution.add(-1)
    assert(result==-1)

    result = solution.add(1)
    assert(result==0)

def run_tests(class_name):
    test_1(class_name)
    test_2(class_name)
    test_3(class_name)
    print("tests passed!")

def main():
    run_tests(KthLargest_2)
    
