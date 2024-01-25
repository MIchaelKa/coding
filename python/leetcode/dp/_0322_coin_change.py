"""
_0322_coin_change

Takeaways:

#dp

"""

from typing import List

class Solution:
    """
        Solution. Naive with full table.

        Complexity:
            time:
            memory:
    """
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        # Can we do better, saving only last max(coins) states?
        # We will need to shift this array each time.
        dp = [-1] * (amount+1)

        for i in range(1, amount+1):
            min_c = amount
            for c in coins:
                j = i-c
                if j < 0:
                    continue
                elif j == 0:
                    dp[i] = 1
                    continue
                elif dp[j] < min_c and dp[j] != -1:
                    min_c = dp[j]
                    dp[i] = min_c+1
            
            # print(dp)

        return dp[-1]

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    coins = [1,2,5]
    amount = 11

    coins = [1,4,5]
    amount = 12

    # coins = [2]
    # amount = 3

    print(coins, amount)
    result = solution.coinChange(coins, amount)
    print(result)