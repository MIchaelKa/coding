"""
_0253_meeting_rooms_2

Takeaways:

Related problems:

TODO:

Tags:
#intervals, #heap

"""

from typing import List

class Solution1:
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

import heapq

class Solution:
    """
        Heap.

        Complexity:
            time: O(n*log(n))
            memory: O(n)
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort() # key=lambda x: x[0]
        heap = [intervals[0][1]]

        for i in range(1, len(intervals)):
            if heap[0] > intervals[i][0]:
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappushpop(heap, intervals[i][1])

        return len(heap)


def main():

    solution = Solution()

    # intervals = [[0,30],[5,10],[15,20]]
    intervals = [[7,10],[2,4]]

    print(intervals)
    result = solution.minMeetingRooms(intervals)
    print(result)


if __name__ == '__main__':
    main()