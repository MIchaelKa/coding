"""
_0078_subsets

Takeaways:

Related problems:

TODO:

Tags:

"""

from typing import List

class Solution_1:
    """
        Backtracking?
        Not optimal

        Complexity:
            time: O()
            memory: O()
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.backtrack(nums, [])
        return self.results
    
    def backtrack(self, available_nums: List[int], current_res: List[int]):

        if not available_nums:
            self.results.append(current_res)
            return

        next = available_nums.pop()

        self.backtrack(list(available_nums), list(current_res))

        current_res.append(next)
        self.backtrack(list(available_nums), current_res)

class Solution_2:
    """
        Backtracking?
        Use index and do not copy nums.

        Complexity:
            time: O(N * 2^N)
            memory: O(N)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.backtrack(nums, [], 0)
        return self.results
    
    def backtrack(self, nums: List[int], current_res: List[int], index: int):

        if index == len(nums):
            self.results.append(current_res)
            return

        self.backtrack(nums, list(current_res), index+1)

        current_res.append(nums[index])
        self.backtrack(nums, current_res, index+1)

class Solution:
    """
        More like a backtracking.

        Complexity:
            time: O()
            memory: O()
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.backtrack(nums, [], 0)
        return self.results
    
    def backtrack(self, nums: List[int], current_res: List[int], index: int):

        if index == len(nums):
            self.results.append(list(current_res))
            return

        self.backtrack(nums, current_res, index+1)

        current_res.append(nums[index])
        self.backtrack(nums, current_res, index+1)
        current_res.pop()

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,2,3]

    print(nums)
    result = solution.subsets(nums)
    print(result)


if __name__ == '__main__':
    main()