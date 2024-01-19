"""
_0150_eval_rpn

Takeaways:

#stack
"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = ['+', '*', '/', '-']

        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.evaluate(a,b,t))
            else:
                stack.append(int(t))

        return stack[0]
    
    def evaluate(self, a, b, op):
        if op == '+': return a + b
        elif op == '*': return a * b
        elif op == '/': return int(a / b)
        elif op == '-': return a - b
        else: print('Not valid operation')

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # tokens = ["2","1","+","3","*"]
    # tokens = ["4","13","5","/","+"]
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    tokens = ["18"]

    print(tokens)
    result = solution.evalRPN(tokens)
    print(result)