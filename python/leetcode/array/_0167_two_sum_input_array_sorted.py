'''
[leetcode] 167. Two Sum II - Input Array Is Sorted

Your solution must use only constant extra space.

_0167_two_sum_input_array_sorted

Tags:
#array, two_pointers

Takeaways:
- in the loop check more likely situation first

'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low = 0
        high = len(numbers) - 1

        while low < high:
            guess = numbers[low] + numbers[high]
            if guess < target:
                low += 1
            elif guess > target:
                high -= 1
            else:
                return[low+1, high+1]

        return []

if __name__ == '__main__':

    solution = Solution()

    numbers = [1,2,4,7,11,15]
    target = 9

    answer = solution.twoSum(numbers, target)
    print(answer)