'''
[leetcode] 22. Generate Parentheses
'''

from typing import List, Set

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = ["()"] # not a set (casting?)
        return list(self.generateParenthesisHelper(strings, n, 1))

    def generateParenthesisHelper(self, strings: Set[str], n: int, k: int) -> List[str]:
        if k == n:
            return strings

        new_strings = set()
        for s in strings:
            new_strings |= self.get_candidates(s) 

        return self.generateParenthesisHelper(new_strings, n, k+1)

    def get_candidates(self, string: str) -> Set[str]:
        strings = set()
        for i in range(len(string)+1):
            strings.add(string[:i]+"()"+string[i:])
        return strings        


if __name__ == '__main__':

    solution = Solution()

    result = solution.generateParenthesis(4)
    print(result)
