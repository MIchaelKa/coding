"""
_0042_trapping_rain_water

Takeaways:
- Previous similar problems are really matter (_0011_container_with_most_water)

#array

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def trap(self, height: List[int]) -> int:

        low = 0
        high = len(height)-1
        current = 0
        min_height = 0
        area = 0

        while low < high:

            if height[low] < height[high]:  
                current = low
                low += 1
            else:
                current = high
                high -= 1

            if height[current] > min_height:
                # +1 or calculate base=(high-low) before updating indexes
                area += (high-low+1) * (height[current]-min_height)
                min_height = height[current]

            area -= min(height[current], min_height)

        return area

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,0,3,2,5]

    print(height)
    result = solution.trap(height)
    print(result)