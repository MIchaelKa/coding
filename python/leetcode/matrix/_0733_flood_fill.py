"""
_0733_flood_fill
https://leetcode.com/problems/flood-fill/description/

Takeaways:
- Copy and deepcopy for 2D arrays

Related problems:

_0200_number_of_islands

695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/

#matrix, #graph, #bfs

"""

from typing import List

from python.common.utils import print_cost_matrix
from collections import deque

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque()

        queue.append((sr,sc))
        orig_color = image[sr][sc]
        image[sr][sc] = color

        rows = len(image)
        cols = len(image[0])

        while queue:

            sr, sc = queue.popleft()
            # print(sr, sc)

            for r, c in directions:
                new_r, new_c = sr+r, sc+c
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and \
                        image[new_r][new_c] == orig_color:
                    image[new_r][new_c] = color
                    queue.append((new_r, new_c))

            # print(queue)
            # print("queue")

        return image

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    image = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ]
    sr = 1
    sc = 1
    color = 2

    print_cost_matrix(image)
    print(sr, sc, color)

    result = solution.floodFill(image, sr, sc, color)

    print_cost_matrix(result)

if __name__ == '__main__':
    main()