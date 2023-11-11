'''
39. Combination Sum

_0039_combination_sum

Tags:
#backtracking

'''

from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        # candidates.sort() # TODO: do we really need sorting?

        def backtrack(solution: List[int], candidates: List[int]):
            nonlocal results

            if accept(solution):
                results.append(solution)
                return
            
            if reject(solution):
                return
            
            for i, c in enumerate(candidates):
                new_cand = candidates[i:] # construct_candidates
                solution.append(c)
                backtrack(list(solution), new_cand)
                solution.pop()

        def accept(solution: List[int]):
            # TODO: remove sum
            return sum(solution) == target

        def reject(solution: List[int]):
            return sum(solution) > target

        backtrack([], candidates)

        return results
    

def main():
    solution = Solution()

    # candidates = [2,3,6,7]
    # target = 7

    candidates = [2,3,5]
    target = 8


    print(candidates, target)
    result = solution.combinationSum(candidates, target)
    print(result)