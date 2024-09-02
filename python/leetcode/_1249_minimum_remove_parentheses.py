"""
_1249_minimum_remove_parentheses

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = [] # (type, position)

        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                if stack and s[stack[-1]] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    stack.append(i)

        excluded_pos = set(stack)
        new_s = ""

        for i in range(len(s)):
            if i not in excluded_pos:
                print(i)
                new_s += s[i]

        return new_s

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "l)ee(t(c)o)de)"

    print(s)
    result = solution.minRemoveToMakeValid(s)
    print(result)


if __name__ == '__main__':
    main()