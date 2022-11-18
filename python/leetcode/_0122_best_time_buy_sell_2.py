"""
[leetcode] 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        last_min = prices[0]
        last_diff = 0

        def close(price):
            nonlocal total, last_min, last_diff
            total += last_diff
            last_min = price
            last_diff = 0

        for i in range(1, len(prices)):
            if prices[i] < last_min:
                close(prices[i])
                continue

            new_diff = prices[i]-last_min
            if new_diff > last_diff:
                last_diff = new_diff
            else:
                close(prices[i])
        
        return total + last_diff


def run_tests(solution):

    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    assert(result==7)
    
    prices = [1,2,3,4,5]
    result = solution.maxProfit(prices)
    assert(result==4)

    print("Tests passed!")

if __name__ == '__main__':

    solution = Solution()
    run_tests(solution)

    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print(result)
