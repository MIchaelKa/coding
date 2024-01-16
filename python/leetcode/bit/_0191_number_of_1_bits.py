"""
_0191_number_of_1_bits

Takeaways:
- n & (n-1) trick

#bit

"""

class Solution:
    """

        Complexity:
            time: O(32)
            memory: O(1)

    """
    def hammingWeight(self, n: int) -> int:

        mask = 1
        counter = 0

        for i in range(0, 32):
            counter += int(mask & n>>i)

        return counter

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    n = 3
    result = solution.hammingWeight(n)
    print(result)