"""
_0134_gas_station

Takeaways:

Related problems:

TODO:

Tags:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff = []
        for g,c in zip(gas, cost):
            diff.append(g-c)

        if (sum(diff) < 0):
            return -1

        print(diff)

        j = 0
        cur_sum = 0
        start_idx = 0

        while j < len(diff):

            idx = start_idx + j
            idx = idx if idx < len(diff) else idx - len(diff)

            cur_sum += diff[idx]

            if cur_sum < 0:
                start_idx = idx+1
                cur_sum = 0
                j = 0    
            else:
                j += 1

        return start_idx

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    gas = [10,1,3]
    cost = [1,11,2]

    print(gas, cost)
    result = solution.canCompleteCircuit(gas, cost)
    print(result)


if __name__ == '__main__':
    main()