from __future__ import annotations

class GraphSolver:

    def __init__(self):
        super().__init__()
        self.verbose = False
        
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        self.discovered = {}
        self.processed = {}

        # После введения этой дополнительной структуры значительно выиграли в скорости
        # и при этом не сильно проиграли в памяти.
        # Почему не сильно проиграли в памяти?
        self.graph = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
             self.graph[i].append(j)

        for i in range(numCourses):
            if i not in self.discovered:
                if self.verbose:
                    print(f"component: {i}")
                if not self.canFinishHelper(i):
                    return False
        
        return True

    def canFinishHelper(self, v: int) -> bool:
        
        self.discovered[v] = True
        
        for p in self.graph[v]:
            if p not in self.discovered:
                if not self.canFinishHelper(p):
                    return False
            if p not in self.processed:
                return False

        self.processed[v] = True

        return True

    
def run_test():
    solver = GraphSolver()
    
    prerequisites = [[1,0],[0,1]]
    numCourses = 2
    assert(solver.canFinish(numCourses, prerequisites)==False)

    prerequisites = [[1,0]]
    numCourses = 2
    assert(solver.canFinish(numCourses, prerequisites)==True)

    prerequisites = [[0,1],[1,2],[2,3],[3,4],[4,1]]
    numCourses = 5
    assert(solver.canFinish(numCourses, prerequisites)==False)

    prerequisites = [[0,1],[1,2],[2,3],[3,4],[0,4]]
    numCourses = 5
    assert(solver.canFinish(numCourses, prerequisites)==True)

    prerequisites = [[0,1],[1,2],[2,3],[3,4],[5,6],[6,7],[7,8],[8,6],[7,3]]
    numCourses = 9
    assert(solver.canFinish(numCourses, prerequisites)==False)

    print("test passed")
        
if __name__ == '__main__':
    run_test()