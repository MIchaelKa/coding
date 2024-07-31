"""
_0528_random_weight

Takeaways:

Related problems:

TODO:

Tags:
#ml

"""

from typing import List
from collections import Counter
import random

class Solution:
    """
        Using random.random()
    """

    def __init__(self, w: List[int]):
        self.w = w
        self.indexes = list(range(len(w)))
        self.indexes.sort(key=lambda idx: self.w[idx])
        self.w.sort()
        self.sum = sum(self.w)
        
        
    def pickIndex(self) -> int:
        r = random.random()
        #index = int(r * len(self.w)) # iniform

        index = len(self.w) - 1
        cur_sum = self.sum
        while index > 0 and r < float(self.w[index]) / cur_sum:
            # print(r, float(self.w[index]) / self.sum)
            cur_sum -= self.w[index] # will we keep the same distribution?
            index -= 1
            r = random.random()
    
        return self.indexes[index]

def main():

    random.seed(2024)

    weigths = [1,3,2]

    solution = Solution(weigths)
    results = []

    for _ in range(10000):
        results.append(solution.pickIndex())

    counter = Counter(results)
    print(counter)


if __name__ == '__main__':
    main()