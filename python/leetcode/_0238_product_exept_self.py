'''
[leetcode] 238. Product of Array Except Self

_0238_product_exept_self

Tags:
#array

Takeaways:
- append can take too much time, better to allocate memory in advance

'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        right_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            right_prod[i] = right_prod[i-1] * nums[-i]

        print(left_prod)
        print(right_prod)

        answer = [left_prod[i] * right_prod[-i-1] for i in range(len(nums))]

        return answer

if __name__ == '__main__':

    solution = Solution()

    nums = [1,2,3,4]
    # nums = [1,2,3,4,5]
    # nums = [8,2,3,4]

    answer = solution.productExceptSelf(nums)
    print(answer)