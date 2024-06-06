"""
_0210_course_schedule_2

Takeaways:

#graph

"""

from typing import List

class Solution:
    """
        DFS. Topological sorting.

        Complexity:
            time:
            memory:
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        self.graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            self.graph[j].append(i)

        self.discovered = [False] * numCourses
        self.processed = [False] * numCourses
        self.courses = []

        for v in range(numCourses):
            if not self.discovered[v]:
                if not self.dfs(v):
                    return []
        
        return self.courses[::-1]
    
    def dfs(self, v: int):

        self.discovered[v] = True

        for y in self.graph[v]:
            if not self.discovered[y]:
                if not self.dfs(y):
                    return False
            elif not self.processed[y]:
                return False
            
        self.processed[v] = True
        self.courses.append(v)
        return True
  


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    prerequisites = [[0,1],[1,4],[1,2],[2,3],[3,4]]
    numCourses = 5

    # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # numCourses = 4

    print(prerequisites)
    result = solution.findOrder(numCourses, prerequisites)
    print(result)

if __name__ == '__main__':
    main()