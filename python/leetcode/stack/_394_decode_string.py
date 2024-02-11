"""
_394_decode_string

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def decodeString(self, s: str) -> str:

        current_str = []
        current_num = []

        stack = []

        for i in range(len(s)):

            if s[i].isnumeric():
                current_num.append(s[i])
                stack.append(''.join(current_str))
                current_str.clear()

            elif s[i] == '[':
                stack.append(''.join(current_num))
                current_num.clear()

            elif s[i] == ']':
                
                local_strs = []
                last = stack.pop(-1)
                while not last.isnumeric():
                    local_strs.append(last)
                    last = stack.pop(-1)

                str_to_repeat = ''.join(local_strs[::-1]) + ''.join(current_str)
                
                repeated_str = str_to_repeat * int(last)
                stack.append(repeated_str)
                current_str.clear()

            else:
                current_str.append(s[i])

        stack.append(''.join(current_str))
        return ''.join(stack)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    s = "qw3[a2[c]d]fe"

    print(s)
    result = solution.decodeString(s)
    print(result)