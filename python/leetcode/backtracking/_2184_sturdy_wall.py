"""
_2184_sturdy_wall
https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/description/

Takeaways:

Related problems:

TODO:

Tags:
#backtracking

"""

from typing import List, Set

class Solution:
    """
        Solution.
        Not works.

        Complexity:
            time: O()
            memory: O()
    """
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:

        self.height = height
        self.width = width
        self.bricks = bricks

        return self.backtrack(set(), 0, 0)


    def backtrack(self, joints: Set[int], pos: int, stage: int) -> int:

        if pos == self.width * 2 and self.height > 1:
            return 1
        
        if pos == self.width and self.height == 1:
            return 1

        if pos > self.width * 2:
            return 0

        if pos > self.width and stage == 0:
            return 0

        num_of_ways = 0

        for b in self.bricks:
            next_pos = pos + b

            # print(next_pos, stage, joints)

            if next_pos-self.width not in joints:

                if next_pos < self.width:
                    joints.add(next_pos)

                new_stage = 1 if stage == 1 or next_pos == self.width else 0
                num_of_ways += self.backtrack(set(joints), next_pos, new_stage)

                # print(f"num_of_ways={num_of_ways}")

                if next_pos in joints and stage == 0:
                    joints.remove(next_pos)

        return num_of_ways



def main():

    solution = Solution()

    height = 2
    width = 3
    bricks = [1,2]

    height = 1
    width = 1
    bricks = [1]

    height = 1
    width = 3
    bricks = [1]

    print(height, width, bricks)
    result = solution.buildWall(height, width, bricks)
    print(result)


if __name__ == '__main__':
    main()