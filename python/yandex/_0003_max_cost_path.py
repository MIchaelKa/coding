"""
_0003_max_cost_path

https://coderun.yandex.ru/problem/print-the-route-of-the-maximum-cost

Takeaways:

#dp

"""

from common.utils import print_cost_matrix


def main():

    N, M = (5, 5)

    cost = [
        [9, 9, 9, 9, 9],
        [3, 0, 0, 0, 0],
        [9, 9, 9, 9, 9],
        [6, 6, 6, 6, 8],
        [9, 9, 9, 9, 9],
    ]

    N, M = (1, 2)

    cost = [
        [9,0]
    ]

    dp = [[0] * M for _ in range(N)]
    dp[0][0] = cost[0][0]

    for i in range(1, M):
        dp[0][i] = dp[0][i-1]+cost[0][i]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0]+cost[i][0]

    for i in range(1, M):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]


    print_cost_matrix(dp)

    i = N-1
    j = M-1

    path = []

    while i != 0 or j != 0:

        if j == 0:
            i -= 1
            path.append('D')
            continue

        if i == 0:
            j -= 1
            path.append('R')
            continue

        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
            path.append('D')      
        else:
            j -= 1
            path.append('R')

    print(' '.join(path[::-1]))
