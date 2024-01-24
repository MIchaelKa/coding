"""
_0210_course_schedule_2

Takeaways:

#graph

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time:
            memory:
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return []

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    prerequisites = [[0,1], [1,4],[1,2],[2,3],[3,4]]
    numCourses = 5

    print(prerequisites)
    result = solution.findOrder(numCourses, prerequisites)
    print(result)