"""
_0528_random_weight

Takeaways:

Related problems:

TODO:
- Use prefix sum (cummulative sum)
- Binary search

Tags:
#ml, #prefix_sum

"""

from typing import List
from collections import Counter
import random
 
class Solution_1:
    """
        Using random.random() each iteration
        Linear search
        Changing distribution
        TLE
    """

    def __init__(self, w: List[int]):
        self.w = w
        # self.indexes = list(range(len(w)))
        # self.indexes.sort(key=lambda idx: self.w[idx])
        # self.w.sort()
        self.sum = sum(self.w)
        
        
    def pickIndex(self) -> int:
        r = random.random()
        #index = int(r * len(self.w)) # iniform

        index = len(self.w) - 1
        cur_sum = self.sum
        # print(r, float(self.w[index]) / cur_sum)
        while index > 0 and r > float(self.w[index]) / cur_sum:
            cur_sum -= self.w[index] # will we keep the same distribution?
            index -= 1
            r = random.random()
            # print(r, float(self.w[index]) / cur_sum)

        # print()
    
        return index#self.indexes[index]
    
class Solution:
    """
        Using random.random() once
        Linear search starting from most probable
    """

    def __init__(self, w: List[int]):

        prefix_sum = [w[0]]
        for i in range(1, len(w)):
            prefix_sum.append(prefix_sum[i-1]+w[i])

        self.sum = prefix_sum[-1]
        self.prefix_sum = prefix_sum
        
    def pickIndex(self) -> int:

        r = random.random() * self.sum

        index = len(self.prefix_sum) - 1
        while index > 0:
            if r > self.prefix_sum[index-1]:
                return index
            index -= 1
        return index

def main():

    random.seed(2024)

    weigths = [1,2,3]
    # weigths = [1,3,2]

    solution = Solution(weigths)
    results = []

    for _ in range(10000):
        results.append(solution.pickIndex())

    counter = Counter(results)
    print(counter)


if __name__ == '__main__':
    main()