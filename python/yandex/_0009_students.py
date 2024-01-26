"""
_0009_students

Takeaways:

#graph

"""

from collections import deque


def main():

    # V, E = tuple(map(int, input().split()))
    # print(V, E)
    # edges = [list(map(int, input().split())) for _ in range(E)]
    # print(edges)

    V, E = (3, 3)
    edges = [
        [1,2],
        [2,3],
        [1,3],
    ]

    V, E = (1, 0)
    edges = [
    ]

    V, E = (9, 7)
    edges = [
        #comp 1
        [1,2],
        [2,3],
        [2,4],
        [4,5],
        [4,6],
        # [6,2],

        # comp 2
        [7,8],
        [8,9],
        # [9,7],
    ]

    result = solver(V, E, edges)
    print('YES' if result else 'NO')

def solver(V, E, edges):

    colors = [-1] * V
    color = 0

    graph = [[] for _ in range(V)]

    for i, j in edges:
        graph[i-1].append(j-1)

    print(graph)

    queue = deque()

    for i in range(V):

        if colors[i] != -1:
            continue

        queue.append(i)
        colors[i] = color

        while queue:

            v = queue.popleft()
            color = colors[v] - color

            # print(colors, color)

            for e in graph[v]:
                # print(e, colors[e], color)
                if colors[e] == -1:
                    colors[e] = color
                    queue.append(e)
                elif colors[e] == colors[v]:
                    return False


    return True