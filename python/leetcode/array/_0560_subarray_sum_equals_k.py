"""
_0560_subarray_sum_equals_k

Takeaways:

TODO:
- Prefix sum + hashmap - DONE

Related problems:
_0238_product_exept_self

Tags:
#prefix_sum

"""

from typing import List

from collections import defaultdict

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
            memory: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        cum_sum = []
        cur_sum = 0
        for n in nums:
            cur_sum += n
            cum_sum.append(cur_sum)

        hashmap = defaultdict(int)
        result = 0

        for i in range(len(nums)-1,-1,-1):
            res = k - nums[i]
            hashmap[cum_sum[i]] += 1
            result += hashmap[res+cum_sum[i]]

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # nums = [1,2,3]
    # k = 3

    nums = [1,2,3,4,5,1,-5,-4,-3,-2]
    k = 1

    # nums = [1,-1,0]
    # k = 0

    print(nums, k)
    result = solution.subarraySum(nums, k)
    print(result)


if __name__ == '__main__':
    main()