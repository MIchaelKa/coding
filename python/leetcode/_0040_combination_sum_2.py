'''
_0040_combination_sum_2

Tags:
#backtracking

'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        candidates.sort()

        def backtrack(solution: List[int], candidates: List[int], total: int):

            if total == target:
                results.append(solution)

            if total > target:
                return
            
            for i, c in enumerate(candidates):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                new_cand = candidates[i+1:] # vs. pop()
                solution.append(c)
                new_total = total + c
                backtrack(list(solution), new_cand, new_total)
                solution.pop()

        backtrack([], candidates, 0)
        
        return results
    

def main():
    solution = Solution()

    # candidates = [10,1,2,7,6,1,5]
    # target = 8

    candidates = [2,5,2,1,2]
    target = 5

    print(candidates, target)
    result = solution.combinationSum2(candidates, target)
    print(result)