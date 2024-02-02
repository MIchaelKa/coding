'''
875. Koko Eating Bananas

_0875_koko_eating_bananas

Tags:
#array, #binary_search

'''

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_speed = max(piles)
        min_speed = 1

        while min_speed < max_speed:
            speed = (max_speed + min_speed) // 2

            hours = 0
            for p in piles:
                hours += (p // speed) + int(p % speed != 0) # ceil

            if hours <= h:
                max_speed = speed
            else:
                min_speed = speed + 1

        return min_speed
    

def main():

    solution = Solution()

    piles = [3,6,7,11]
    h = 8

    piles = [30,11,23,4,20]
    h = 5

    result = solution.minEatingSpeed(piles, h)
    print(result)
