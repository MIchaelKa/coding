"""
_0721_accounts_merge

Takeaways:
- we need to get edges to use union_find

TODO:

Related problems:
_0684_redundant_connection

Tags:
#union_find

"""

from typing import List
from collections import deque

class Solution_1:
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
    

from collections import defaultdict

class Solution:
    """
        DFS.

        Complexity:
            time: O(m=n*k) total_emails = num_acc * max_size
            memory: O(m)
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def dfs(start_email, all_emails):
            if start_email not in visited:
                visited.add(start_email)
                all_emails.append(start_email)
                for e in graph[start_email]:
                    dfs(e, all_emails)


        graph = defaultdict(list)

        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                graph[first_email].append(account[i])
                graph[account[i]].append(first_email)

        visited = set()
        result = []

        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in visited:
                new_account = [name]
                emails = []
                dfs(first_email, emails)
                result.append(new_account+sorted(emails))

        return result

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

    accounts = [
        ["A","1","2"],
        ["B","3","4"],
        ["A","5","6"],
        ["A","6","1"],
        ["B","7","8"],
    ]

    print(accounts)
    result = solution.accountsMerge(accounts)
    print(result)


if __name__ == '__main__':
    main()