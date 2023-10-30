'''
[leetcode] 347. Top K Frequent Elements

_0347_top_k_freq_elem

#array, #heap, #bucket_sort

'''

from typing import List
from collections import defaultdict
import heapq

class Solution_1:
    """
        Solution_1.
        Naive solution. 
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        result = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        result = [x[0] for x in result]

        return result

class Solution_2:
    """
        Solution_2.
        Using python heapq

        Если не использовать heapify, а только heappush.
        Тогда нужно уметь искать уже добавленные ключи.
        Но в heapq нет эффективного поиска.
    
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        heap = [(-x[1], x[0]) for x in counter.items()]
        heapq.heapify(heap)

        # convert to output list
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

class Solution_3:
    """
        Solution_3.
        Use python heapq more wisely
    
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        #
        # the implementation below is exactly that heapq.nlargest do
        #

        counter = list(counter.items())
        heap = []
    
        # put first k keys into heap
        for i in range(k):
            c = counter[i]
            heapq.heappush(heap, (c[1], c[0]))

        # push/pop other elements
        for i in range(k, len(counter)):
            c = counter[i]
            heapq.heappush(heap, (c[1], c[0]))
            heapq.heappop(heap)

        # convert to output list
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


if __name__ == '__main__':

    solution = Solution_3()

    # nums = [1,1,1,1,2,2,3,3,3]
    # k = 2

    # nums = [1]
    # k = 1

    nums = [1,1,1,1,2,2,3,3,3,4,5,6,7,7,7,7,7,7,7]
    k = 3

    result = solution.topKFrequent(nums, k)
    print(result)
