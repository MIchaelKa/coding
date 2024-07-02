"""
_0253_meeting_rooms_2

Takeaways:

Related problems:

TODO:

Tags:
#intervals, #heap

"""

from typing import List

class Solution:
    """
        Naive.

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort() # key=lambda x: x[0]

        meeting_ends = [intervals[0][1]]

        for i in range(1, len(intervals)):

            j = 0 
            while j < len(meeting_ends):
                if meeting_ends[j] <= intervals[i][0]:
                    break
                j += 1

            if j < len(meeting_ends):
                meeting_ends[j] = intervals[i][1]
            else:
                meeting_ends.append(intervals[i][1])

        return len(meeting_ends)


def main():

    solution = Solution()

    intervals = [[0,30],[5,10],[15,20]]

    print(intervals)
    result = solution.minMeetingRooms(intervals)
    print(result)


if __name__ == '__main__':
    main()