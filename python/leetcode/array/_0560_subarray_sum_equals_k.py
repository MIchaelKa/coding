"""
_0560_subarray_sum_equals_k

Takeaways:

TODO:
- Prefix sum + hashmap

Related problems:
Tags:
#prefix_sum

"""

from typing import List

class Solution:
    """
        Naive.

        Complexity:
            time: O(n^2 ?)
            memory: O(1)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum == k:
                    result += 1
        return result
    
class Solution:
    """
        Prefix sum + hashmap

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1,2,3]
    k = 3

    nums = [1,2,3,4,5,1,-5,-4,-3,-2]
    k = 1

    print(nums, k)
    result = solution.subarraySum(nums, k)
    print(result)


if __name__ == '__main__':
    main()