"""
[leetcode] 11. Container With Most Water
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

        while start != end:
            base = end-start
            if height[start] < height[end]:
                min_height = height[start]
                start += 1
            else:
                min_height = height[end]
                end -= 1

            area = base * min_height
            if area > max_area:
                max_area = area

        return max_area


if __name__ == '__main__':
    solution = Solution2()
    height = [1,8,6,2,5,4,8,3,7]
    result = solution.maxArea(height)
    print(result)