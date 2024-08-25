"""
_0624_task_scheduler

Takeaways:

TODO:

Related problems:

Tags:
#heap

"""

from typing import List
from collections import Counter

import heapq

class Solution:
    """
        Solution.

        Complexity:
            time: O(n*log(n))
            memory: O(n)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        intervals = 0

        heap = [(-v,k) for k,v in counter.items()]
        heapq.heapify(heap)

        final_tasks = []

        while heap:

            tasks = len(heap)
            add_to_heap = []

            for _ in range(min(n+1, tasks)):
                v, k = heapq.heappop(heap)
                final_tasks.append(k)
                v += 1
                if v < 0:
                    add_to_heap.append((v, k))

            for v, k in add_to_heap:
                heapq.heappush(heap, (v, k)) # O(log(n))

            intervals += n+1 if heap else tasks
            print(intervals, final_tasks)
        
        return intervals

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    tasks = ["A","A","A","B","B","B"]
    n = 2

    # tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    # n = 1

    # tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
    # n = 2

    # tasks = ["A","A","A","B","B","B", "C","C", "D", "D"]
    # n = 2

    print(tasks, n)
    result = solution.leastInterval(tasks, n)
    print(result)


if __name__ == '__main__':
    main()