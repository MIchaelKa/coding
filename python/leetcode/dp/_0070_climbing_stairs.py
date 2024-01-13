"""
_0070_climbing_stairs

#dp

Note: the solution is fibonacci number

"""

class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        prev_0 = 1
        prev_1 = 1
        result = 0

        for i in range(0, n-1):
            result = prev_1 + prev_0
            prev_0 = prev_1
            prev_1 = result

        return result

def main():
    solution = Solution()

    result = solution.climbStairs(5)
    print(result)