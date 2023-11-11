'''
[leetcode] 739. Daily Temperatures

_0739_daily_temp

Tags:
#array, #stack

'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = [None]

        for i, t in enumerate(temperatures):
            last = stack[-1]
            while last is not None and t > last[0]:
                answer[last[1]] = i - last[1]
                stack.pop()
                last = stack[-1]
            stack.append((t,i))

            # print(stack)

        return answer
    


def main():

    solution = Solution()

    # temperatures = [73,74,75,71,69,72,76,73]
    temperatures = [30,40,50,60]

    result = solution.dailyTemperatures(temperatures)
    print(result)