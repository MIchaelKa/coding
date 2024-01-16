"""
_0136_single_number

#bit

"""

from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            mask ^= n
        return mask


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [4,1,2,1,2,7,8,12,8,12,7]

    print(nums)
    result = solution.singleNumber(nums)
    print(result)