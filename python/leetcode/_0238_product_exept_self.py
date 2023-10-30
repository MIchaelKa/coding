'''
[leetcode] 238. Product of Array Except Self

_0238_product_exept_self

#array

'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = [nums[0]]
        for i in range(1, len(nums)):
            left_prod.append(left_prod[i-1]*nums[i])

        right_prod = [nums[-1]]
        for i in range(1, len(nums)-1):
            right_prod.append(right_prod[i-1]*nums[-i-1])

        answer = []
        for i in range(len(nums)):
            result = 1
            if i > 0:
                result *= left_prod[i-1]
            if i < len(nums)-1:
                result *= right_prod[-i-1]
            answer.append(result)

        return answer

if __name__ == '__main__':

    solution = Solution()

    nums = [1,2,3,4]
    # nums = [1,2,3,4,5]

    answer = solution.productExceptSelf(nums)
    print(answer)