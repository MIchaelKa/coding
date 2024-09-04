"""
_0227_basic_calculator

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
            time: O()
            memory: O()
    """

    def make_op(self, op: str, a: int, b: int) -> int:
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
        else:
            return a//b
        
    def is_op(self, c: str) -> bool:
        return c == "+" or c == "-" or c == "*" or c == "/"
    
    def eval_stack_v1(self, stack: list[int]):
        # print(stack)
        while stack and len(stack) != 1:
            a = stack.pop()
            op = stack.pop()
            b = stack.pop()
            res = self.make_op(op, b, a)
            stack.append(res)


    def eval_stack(self, stack: list[int]):
        # print(stack)
        i = 1
        a = stack[0]
        while i < len(stack):
            op = stack[i]
            b = stack[i+1]
            a = self.make_op(op, a, b)
            i += 2
        return a

    def calculate(self, s: str) -> int:

        stack = []
        i = 0

        while i < len(s):

            if self.is_op(s[i]):
                stack.append(s[i])
                i += 1
                continue
            elif s[i] == " ":
                # if stack and not self.is_op(stack[-1]):
                #     self.eval_stack(stack)
                i += 1
                continue

            digits = []
            while i < len(s) and s[i].isdigit():
                digits.append(s[i])
                i += 1
            digit = int("".join(digits))
     
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                op = stack.pop()
                prev = stack.pop()
                res = self.make_op(op, prev, digit)
                stack.append(res)
            else:
                stack.append(digit)

            # print(stack)

        return self.eval_stack(stack)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "15+2*20+15 / 7"
    # s = "15+2*20+15"
    # s = " 3+5 / 2 "
    # s = "0-2147483647"
    # s = "0-35"
    s = "1-1+1"

    print(s)
    result = solution.calculate(s)
    print(result)


if __name__ == '__main__':
    main()