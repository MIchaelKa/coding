"""
_0332_reconstruct_itinerary

Takeaways:
- defaultdict of defaultdict
- dfs + heap

TODO:
- Add condition to detect that we found optimal path

"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    """
        DFS and backtracking.

        Complexity:
            time: O((E+V)^d), d - the max number of flights from an airport
            memory: O(E+V)
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        self.discovered = defaultdict(lambda: defaultdict(int))
        self.result = []

        for i, j in tickets:
            self.discovered[i][j] += 1

        self.dfs('JFK')
        return self.result
    
    def dfs(self, v: str):

        self.result.append(v)
  
        # TODO: better to sort all tickets at the begining
        edges = [key for key, val in self.discovered[v].items() if val > 0]
        heapq.heapify(edges)

        while edges:
            edge = heapq.heappop(edges)
            self.discovered[v][edge] -= 1
            if self.dfs(edge):
                return True      
            self.discovered[v][edge] += 1
        
        # TODO: is it possible to make this check more optimal?
        # 1 - check for the case when we found solution
        # 2 - more optimal check for bad case
        for i in self.discovered.values():
            for j in i.values():
                if j > 0:
                    self.result.pop(-1)
                    return False

        return True


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

    print(tickets)
    result = solution.findItinerary(tickets)
    print(result)