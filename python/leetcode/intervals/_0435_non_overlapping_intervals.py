"""
_0435_non_overlapping_intervals

Takeaways:

Related problems:

#intervals

"""

from typing import List

class Solution:
    """
        Greedy.
        Earliest end time.

        Complexity:
            time: O(n*log(n)) - sorting
            memory: O(1)
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        last_interval_end = intervals[0][1]
        count = 1

        for interval in intervals[1:]:
            if  interval[0] >= last_interval_end:
                last_interval_end = interval[1]
                count += 1

        return len(intervals) - count

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    intervals = [[1,2],[2,3],[3,4],[1,3]]
    intervals = [[1,2],[2,3],[3,4]]

    intervals = [[1,2],[1,7],[2,3]]

    print(intervals)
    result = solution.eraseOverlapIntervals(intervals)
    print(result)

if __name__ == '__main__':
    main()