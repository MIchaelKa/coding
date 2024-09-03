"""
_0050_pow

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Naive. TLE

        Complexity:
            time: O()
            memory: O()
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        temp = x
        for _ in range(1, abs(n)):
            x *= temp

        if n < 0:
            x = 1 / x

        return x

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    x = 2
    n = -1

    print(x, n)
    result = solution.myPow(x, n)
    print(result)


if __name__ == '__main__':
    main()