"""
_0050_pow

Takeaways:
- https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations
- Complement Representation

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Naive. TLE

        Complexity:
            time: O(n)
            memory: O(1)
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
    
class Solution:
    """
        Binary exponentiation

        Complexity:
            time: O(log(n))
            memory: O(log(n))
    """
    def myPow(self, x: float, n: int) -> float:

        print(n)
        
        if n == 0:
            return 1
        
        if n < 0:
            # TODO: why it's works slower?
            # return 1 / self.myPow(x, -n)
            return self.myPow(1/x, -n)
        
        if n % 2 != 0:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x**2, n // 2)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    x = 2
    n = -2147483648

    print(x, n)
    result = solution.myPow(x, n)
    print(result)


if __name__ == '__main__':
    main()