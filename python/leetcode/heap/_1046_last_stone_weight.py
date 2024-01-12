"""
_1046_last_stone_weight

#heap

"""

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        min_heap = [-s for s in stones]
        heapq.heapify(min_heap)

        while len(min_heap) >= 2:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)

            if first == second:
                continue

            # TODO: abs is not needed since we know first >= second
            diff = -abs(first - second)
            heapq.heappush(min_heap, diff)

        result = -min_heap[0] if len(min_heap) > 0 else 0

        return result
    

def main():

    solution = Solution()

    stones = [2,7,4,1,8,1]
    # stones = []

    result = solution.lastStoneWeight(stones)
    print(result)