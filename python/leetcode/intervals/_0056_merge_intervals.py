"""
_0056_merge_intervals

#intervals

"""

from typing import List

class Solution:
    """
        Solution 1
        Using sort
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        cur_interval = intervals[0]
        result = []

        for i in range(1, len(intervals)):

            if cur_interval[1] < intervals[i][0]:
                result.append(cur_interval)
                cur_interval = intervals[i]
            else:
                cur_interval = [
                    min(cur_interval[0], intervals[i][0]),
                    max(cur_interval[1], intervals[i][1])
                ]

        if len(result) == 0 or cur_interval != result[-1]:
            result.append(cur_interval)

        return result
        


def main():
    solution = Solution()

    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]]
    intervals = [[1,4],[0,0]]

    result = solution.merge(intervals)
    print(intervals)
    print(result)