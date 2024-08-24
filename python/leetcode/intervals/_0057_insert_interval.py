"""
_0057_insert_interval

#intervals

Hints:
- update newInterval variable during iteration - Done

"""

from typing import List

class Solution_1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]
        
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        result = []

        new_start = None

        for i in intervals:
            
            if new_start is None:
                if newInterval[0] >= i[0] and newInterval[0] <= i[1]:
                    new_start = i[0]
                elif newInterval[1] >= i[0] and newInterval[1] <= i[1]:
                    new_start = newInterval[0]
                elif newInterval[0] <= i[0] and newInterval[1] > i[1]:
                    new_start = newInterval[0]
                elif newInterval[0] <= i[0] and result[-1][1] < newInterval[0]:
                    new_start = newInterval[0]

            if new_start is not None: 
                if newInterval[1] >= i[0] and newInterval[1] <= i[1]:
                    result.append([new_start, i[1]])
                    new_start = None
                    continue
                elif newInterval[1] < i[0]:
                    result.append([new_start, newInterval[1]])
                    new_start = None

            if new_start is None:
                result.append(i)

        if new_start is not None:
            result.append([new_start, newInterval[1]])
     
        return result

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for interval in intervals:

            if newInterval and newInterval[1] < interval[0]:
                result.append(newInterval)
                result.append(interval)
                newInterval = None
                continue

            if not newInterval or newInterval[0] > interval[1]:
                result.append(interval)
                continue

            newInterval = [
                min(newInterval[0], interval[0]),
                max(newInterval[1], interval[1])
            ]
                
        if newInterval:
            result.append(newInterval)

        return result



def run_tests(solution):

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    result = solution.insert(intervals, newInterval)
    print(result)
    assert(result == [[1, 2], [3, 10], [12, 16]])

    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    result = solution.insert(intervals, newInterval)
    assert(result == [[1, 5], [6, 9]])

    intervals = []
    newInterval = [2,5]
    result = solution.insert(intervals, newInterval)
    assert(result == [[2,5]])

    intervals = [[1,5]]
    newInterval = [2,3]
    result = solution.insert(intervals, newInterval)
    assert(result == [[1,5]])

    intervals = [[1,5]]
    newInterval = [2,7]
    result = solution.insert(intervals, newInterval)
    assert(result == [[1, 7]])

    intervals = [[1,5]]
    newInterval = [6,8]
    result = solution.insert(intervals, newInterval)
    assert(result == [[1, 5], [6, 8]])

    intervals = [[1,5]]
    newInterval = [0,3]
    result = solution.insert(intervals, newInterval)
    assert(result == [[0, 5]])

    intervals = [[1,5]]
    newInterval = [0,0]
    result = solution.insert(intervals, newInterval)
    assert(result == [[0, 0], [1, 5]])

    intervals = [[1,5]]
    newInterval = [0,6]
    result = solution.insert(intervals, newInterval)
    assert(result == [[0, 6]])

    intervals = [[3,5],[12,15]]
    newInterval = [6,6]
    result = solution.insert(intervals, newInterval)
    assert(result == [[3, 5], [6, 6], [12, 15]])

    print("tests passed!")     

def main():
    solution = Solution()

    run_tests(solution)

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    result = solution.insert(intervals, newInterval)
    print(intervals, newInterval)
    print(result)

if __name__ == '__main__':
    main()