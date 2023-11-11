'''
_0040_combination_sum_2

Notes:
Can we benefit from optimizing the search with BFS or A*?

This problem is the same problem as the subset sum problem, which is a famous np-complete problem.
The only solution is the brute force solution.

Tags:
#backtracking

'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        candidates.sort()
        print(candidates)

        def backtrack(solution: List[int], pos: int, total: int):

            if total == target:
                results.append(list(solution))

            if total > target:
                return
            
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue

                # outside of reject method if it was
                if candidates[i] > target:
                    break

                solution.append(candidates[i])
                # print(solution, pos+i+1)
                backtrack(solution, i+1, total+candidates[i])
                solution.pop()

        backtrack([], 0, 0)
        
        return results
    

def main():
    solution = Solution()

    candidates = [10,1,2,7,6,1,5]
    target = 8

    # candidates = [2,5,2,1,2]
    # target = 5

    print(candidates, target)
    result = solution.combinationSum2(candidates, target)
    print(result)