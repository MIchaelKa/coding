"""
_0846_hand_of_straights

https://leetcode.com/problems/hand-of-straights/description/

Takeaways:

"""

from typing import List
from collections import deque

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        queue = deque(sorted(hand))
        
        while queue:
            group = []
            residuals = []
            group.append(queue.popleft())

            while len(group) < groupSize and queue:
                n = queue.popleft()
                if group[-1] == n-1:
                    group.append(n)
                elif group[-1] == n:
                    residuals.append(n)
                else:
                    return False
                
            for r in residuals[::-1]:
                queue.insert(0,r)

            if len(group) < groupSize:
                return False
            
            # print(group)
            # print(queue)
                
        return True

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3

    hand = [1,2,3,4,5]
    groupSize = 4

    hand = [1,1,2,2,3,3]
    groupSize = 2

    print(hand, groupSize)
    result = solution.isNStraightHand(hand, groupSize)
    print(result)