'''
875. Koko Eating Bananas

_0875_koko_eating_bananas

https://leetcode.com/problems/koko-eating-bananas

Takeaways:
+/-1 in binary_search do not really affect time performance

Tags:
#array, #binary_search

'''

from typing import List
import math

class Solution:
    """
        Solution.

        Complexity:
            time: O(n*log(n))
            memory: O(1)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_speed = max(piles)
        min_speed = 1
        result = max_speed

        while min_speed <= max_speed:
            speed = (max_speed + min_speed) // 2

            hours = 0
            for p in piles:
                # hours += (p // speed) + int(p % speed != 0) # ceil
                hours += math.ceil(float(p) / speed)

            if hours <= h:
                max_speed = speed - 1
                result = speed
            else:
                min_speed = speed + 1

        return result
    

def main():

    solution = Solution()

    piles = [3,6,7,11]
    h = 8

    # piles = [30,11,23,4,20]
    # h = 5

    piles = [30,11,23,4,20]
    h = 6

    result = solution.minEatingSpeed(piles, h)
    print(result)
