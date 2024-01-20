"""
_853_car_fleet

Takeaways:

#arrat, #stack

"""

from typing import List

class Solution:
    """
        Solution.

        TODO: Improve solution removing stack and make it O(1)

        Complexity:
            time: O(n*log(n)) - sort
            memory: O(n)
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        indexes = list(range(len(position)))
        indexes.sort(key=lambda i: position[i], reverse=True)

        # print(indexes)

        for i in indexes:
            dist = target-position[i]
            moves = dist / speed[i]

            # print(moves)

            if len(stack)==0:
                stack.append((moves, speed[i]))
            else:
                last_m, last_s = stack[-1]
                if moves <= last_m:
                    stack[-1] = (last_m, min(speed[i], last_s))
                else:
                    stack.append((moves, speed[i]))

            # print(stack)

        return len(stack)

def run_tests(solution):
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    assert(solution.carFleet(target, position, speed) == 3)

    target = 10
    position = [3]
    speed = [3]
    assert(solution.carFleet(target, position, speed) == 1)
    
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    assert(solution.carFleet(target, position, speed) == 1)

    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    target = 10
    position = [8,3,7,4,6,5]
    speed = [4,4,4,4,4,4]

    print(target, position, speed)
    result = solution.carFleet(target, position, speed)
    print(result)