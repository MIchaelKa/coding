"""
_0721_accounts_merge

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List
from collections import deque

class Solution:
    """
        Brute force.

        Complexity:
            time: O(N^2)
            memory: O(N)
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        queue = deque(accounts)

        for _ in range(len(queue)):
            root = queue.popleft()
            root_name = root[0]
            root_acc = set(root[1:])

            for _ in range(len(queue)):
                merge = queue.popleft()
                merge_name = merge[0]
                merge_acc = set(merge[1:])

                if merge_name == root_name and root_acc & merge_acc:
                    root_acc |= merge_acc
                else:
                    queue.append(merge)

            queue.append([root_name]+sorted(list(root_acc)))

        return list(queue)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]

    print(accounts)
    result = solution.accountsMerge(accounts)
    print(result)


if __name__ == '__main__':
    main()