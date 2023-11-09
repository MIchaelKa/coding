"""
[skiena] 9.1 Derangements
Backtracking search for all derangements.

Как правильно настроить отсечения?
Подход 1.
Классический вариант просто завести метод reject()

Подход 2.
А что если не выдавать в доступных кандидатах для выбора этот элемент вообще?
Но тогда как прокидывать вариант вниз по стеку вызовов?
Использовать глобальные переменные?

_09_01_derangements

Tags:
#backtracking

"""

class Solution:

    def derangements(self, n: int):
        solution = [None] * n
        candidates = list(range(n+1))[1:]   
        self.backtrack(solution, candidates, 0, n)

    def backtrack(self, solution: list[int], candidates: list[int], k: int, n: int):

        # remove reject to get all permutations
        if self.reject(solution):
            return

        if self.accept(k, n):
            self.process_solution(solution)
            return

        for i in range(len(candidates)):
            new_cand = list(candidates) # shallow copy
            solution[k] = new_cand.pop(i) # make move
            self.backtrack(solution, new_cand, k+1, n)
            solution[k] = None # unmove

    def reject(self, solution: list[int]):
        for i in range(len(solution)):
            if solution[i] == i+1:
                return True
        return False

    def accept(self, k: int, n: int) -> bool:
        if k == n:
            return True
        return False

    def process_solution(self, data: list[int]):
        print(data)

def main():
    solution = Solution()
    solution.derangements(4)
 