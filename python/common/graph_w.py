from __future__ import annotations
from collections import deque

from union_set import UnionSet

import graph_builder as gb

MAX_WEIGHT = 100
MAX_NUM_VERT = 10

class Edge:
    def __init__(self, v: int, weight: int):
        self.v = v
        self.weight = weight

class EdgePair:
    def __init__(self, x: int, y: int, weight: int):
        self.x = x
        self.y = y
        self.weight = weight

class GraphW():

    def __init__(self, directed: bool = False, num_vertices: int = MAX_NUM_VERT):
        self.verbose = False

        self.directed = directed
        self.num_vertices = num_vertices
        self.edges = [[] for _ in range(self.num_vertices)]
        self.edge_array = []

    def insert_edge(self, x: int, y: int, weight: int = 1) -> None:
        self.edges[x].append(Edge(y, weight))

    def bfs(self, start: int) -> None:
        """
        Performs breadth-first search/traversal (BFS) on the graph
        
        Args:
            start (int): The vertex to start with (Root vertex).
        """
        
        processed = [False] * self.num_vertices
        discovered = [False] * self.num_vertices
        self.parent = [-1] * self.num_vertices
        
        queue = deque()
        
        discovered[start] = True
        queue.append(start)
        
        while queue:
            vertex = queue.popleft()
            self.process_vertex_early(vertex)
            
            processed[vertex] = True # should we move it after process_vertex_late?
            
            vertex_edges = self.edges[vertex] # will it speed it up?
            
            for edge in vertex_edges:
                y = edge.v
                if not processed[y] or self.directed:
                    self.process_edge(vertex, y, edge.weight)
                
                if not discovered[y]:
                    queue.append(y)  # what about += and add all vertices at one time?
                    discovered[y] = True
                    self.parent[y] = vertex
                    
            self.process_vertex_late(vertex)
    
    def process_vertex_early(self, vertex: int) -> None:
        if self.verbose:
            print(f"process_vertex_early: {vertex}")
    
    def process_vertex_late(self, vertex: int) -> None:
        if self.verbose:
            print(f"process_vertex_late: {vertex}\n")

    def process_edge(self, x: int, y: int, weight: int) -> None:
        if self.verbose:
            print(f"process_edge: {x}-{y} [{weight}]")
        self.edge_array.append(EdgePair(x,y,weight))


    def kruscal(self):

        union_set = UnionSet(self.num_vertices)

        self.bfs(0)

        self.edge_array.sort(key=lambda k: k.weight)
        
        mst_edges = []
        for e in self.edge_array:
            if not union_set.same_component(e.x, e.y):
                union_set.union(e.x, e.y)
                mst_edges.append(e)

        for e in mst_edges:
            print(f"MST edge: {e.x}-{e.y} [{e.weight}]")

    
    def prim(self):

        intree = [False] * (self.num_vertices)
        distance = [MAX_WEIGHT] * (self.num_vertices)
        self.parent = [-1] * (self.num_vertices)

        start = 0
        v = start

        # stops when we will not able to update v
        while not intree[v]:

            intree[v] = True

            if v != start:
                print(f"MST edge: {self.parent[v]}-{v} [{dist}]")

            # Операция присоединения нового ребра к MST
            # Проверяем ребра только тут и запоминаем информацию о 
            # самом лучшем варианте для присоединения данной вершины
            for edge in self.edges[v]:
                if edge.weight < distance[edge.v] and not intree[edge.v]:
                    distance[edge.v] = edge.weight
                    # Cама операция присоединения - установка родителя.
                    # - Почему тут, ведь мы совершаем лишнюю работу?
                    # - Потому что только тут еще есть информация о родителе,
                    # так как мы не всегда присоединяем следующий лист с текущего v
                    self.parent[edge.v] = v
            
            # Выбираем следующую вершину на присоединение.
            # - Чтобы проверить этот массив все равно совершаем О(n) операций - проверяем все вершины ?!
            # - Да, - иначе был бы поиск по всем ребрам О(m)!
            dist = MAX_WEIGHT
            for i in range(self.num_vertices):
                if not intree[i] and distance[i] < dist:
                    dist = distance[i]
                    v = i

            # TODO: prints the last edge two times
            # print(v)

        print(self.parent)

    def find_path(self, v: int) -> list[int]:

        if self.parent[v] == -1:
            return [v]

        path = self.find_path(self.parent[v])
        path.append(v)
        return path
    
    def dijkstra(self):

        intree = [False] * (self.num_vertices)
        distance = [MAX_WEIGHT] * (self.num_vertices)
        self.parent = [-1] * (self.num_vertices)

        start = 0
        distance[start] = 0
        v = start

        while not intree[v]:

            intree[v] = True

            if v != start:
                if self.verbose:
                    print(f"edge: {self.parent[v]}-{v} [{dist}]")

            for edge in self.edges[v]:
                new_dist = edge.weight + distance[v]
                if new_dist < distance[edge.v] and not intree[edge.v]:
                    distance[edge.v] = new_dist
                    self.parent[edge.v] = v
            
            dist = MAX_WEIGHT
            for i in range(self.num_vertices):
                if not intree[i] and distance[i] < dist:
                    dist = distance[i]
                    v = i

    def edge_iter(self):
        for v in range(self.num_vertices):
            for edge in self.edges[v]:
                yield v, edge.v, edge.weight

    def bellman_ford(self, source: int):

        self.distance = [MAX_WEIGHT] * (self.num_vertices)
        self.parent = [-1] * (self.num_vertices)

        self.distance[source] = 0

        for _ in range(self.num_vertices-1):
            for u, v, w in self.edge_iter():
                new_dist = w + self.distance[u]
                if new_dist < self.distance[v]:
                    self.distance[v] = new_dist
                    self.parent[v] = u

        # Detect if negative cycles is present
        ret_val = True
        for u, v, w in self.edge_iter():
            new_dist = w + self.distance[u]
            if new_dist < self.distance[v]:
                if self.verbose:
                    print(f"nc edge {u}-{v} [{self.distance[v]}]")
                ret_val = False
                
        return ret_val
    
    def bellman_ford_min_paths(self):
        """
        Cormen [22.1-6]
        Find minimum distance for any possible path(from any start vertex) for all verticies.
        If no such paths exist return MAX_WEIGHT for this vertex, which means that
        this vertex is not reachable from anywhere.
        """

        self.distance = [MAX_WEIGHT] * (self.num_vertices)
        self.parent = [-1] * (self.num_vertices)

        for _ in range(self.num_vertices-1):
            for u, v, w in self.edge_iter():
                new_dist = min(w + self.distance[u], w)
                if new_dist < self.distance[v]:
                    self.distance[v] = new_dist
                    # FIXME: parent do not set right
                    self.parent[v] = u
                        
        return True


if __name__ == '__main__':
    
    g = gb.build_graph_from_file("graph_d_w_4")
    g.verbose = True

    result = g.bellman_ford_min_paths()
    print(result)
    # print(g.find_path(6))
    print(g.parent)
    print(g.distance)
