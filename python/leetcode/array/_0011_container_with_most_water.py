"""
[leetcode] 11. Container With Most Water
_0011_container_with_most_water

#array

"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_area = 0

        while start != end:
            max_area = max(max_area, (end-start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
    
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1

        max_area = 0
        start_height = -1
        end_height = -1

        while start != end:
            if height[start] < height[end]:
                min_height = height[start]
                if min_height > start_height:
                    max_area = max(max_area, (end-start) * min_height)
                    start_height = min_height
                start += 1
            else:
                min_height = height[end]
                if min_height > end_height:
                    max_area = max(max_area, (end-start) * min_height)
                    end_height = min_height
                end -= 1

        return max_area


def main():
    solution = Solution2()
    height = [1,8,6,2,5,4,8,3,7]

    print(height)
    result = solution.maxArea(height)
    print(result)