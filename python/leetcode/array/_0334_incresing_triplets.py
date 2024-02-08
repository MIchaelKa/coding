"""
_0334_incresing_triplets

Takeaways:

"""

from typing import List

class Solution:
    """
        Solution.
        TLE

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:

        cache = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(1, i+1):
                if nums[i] > nums[i-j]:
                    cache[i] = max(cache[i], cache[i-j]+1)
                    if cache[i] == 3:
                        return True

        return False

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [10,100,12,9,10,2,11,13]
    nums = [10,100,12,9,10,2,10,9]

    print(nums)
    result = solution.increasingTriplet(nums)
    print(result)