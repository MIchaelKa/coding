"""
[leetcode] 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

"""

from typing import List

"""
Solutions 1-3 - One pass
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        diff = 0
        for i in range(1, len(prices)):
            diff = max(diff, prices[i]-min_p)
            min_p = min(min_p, prices[i])
        return diff

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i]-min_p > diff:
                diff = prices[i]-min_p
        return diff

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            else:
                new_diff = prices[i]-min_p
                if new_diff > diff:
                    diff = new_diff
        return diff

if __name__ == '__main__':

    solution = Solution3()

    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print(result)

