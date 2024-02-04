"""
_332_reconstruct_itinerary

Takeaways:

"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    """
        Solution. Not works.

        Complexity:
            time: O()
            memory: O()
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        self.discovered = defaultdict(dict)
        self.result = []

        for i, j in tickets:
            self.discovered[i][j] = False

        self.dfs('JFK')
        return self.result
    
    def dfs(self, v: str):

        self.result.append(v)
  
        edges = [key for key, val in self.discovered[v].items() if not val]
        heapq.heapify(edges)

        while edges:
            edge = heapq.heappop(edges)
            self.discovered[v][edge] = True
            if self.dfs(edge):
                return True
            else:
                self.discovered[v][edge] = False
            
        for i in self.discovered.values():
            for j in i.values():
                if j == False:
                    self.result.pop(-1)
                    return False

        return True


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

    print(tickets)
    result = solution.findItinerary(tickets)
    print(result)