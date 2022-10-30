from __future__ import annotations
from collections import deque

from union_set import UnionSet

def init_grapth_1(g: GraphW) -> GraphW:
    g.num_vertices = 7

    g.insert_edge(0,1,weight=5)
    g.insert_edge(0,2,weight=7)
    g.insert_edge(0,3,weight=12)
    
    
    g.insert_edge(1,0,weight=5)
    g.insert_edge(1,2,weight=1) # 9, 1
    g.insert_edge(1,4,weight=7)

    g.insert_edge(2,0,weight=7)
    g.insert_edge(2,1,weight=1) # 9, 1
    g.insert_edge(2,4,weight=4)
    g.insert_edge(2,5,weight=3)
    g.insert_edge(2,3,weight=4)

    g.insert_edge(3,0,weight=12)
    g.insert_edge(3,2,weight=4)
    g.insert_edge(3,5,weight=7)
    
    g.insert_edge(4,1,weight=7)
    g.insert_edge(4,2,weight=4)
    g.insert_edge(4,5,weight=2)
    g.insert_edge(4,6,weight=5)

    g.insert_edge(5,2,weight=3)
    g.insert_edge(5,3,weight=7)
    g.insert_edge(5,4,weight=2)
    g.insert_edge(5,6,weight=2)

    g.insert_edge(6,4,weight=5)
    g.insert_edge(6,5,weight=2)
    
    return g

def init_grapth_2(g: GraphW) -> GraphW:
    g.num_vertices = 5

    g.insert_edge(0,1,weight=4)
    g.insert_edge(0,2,weight=5)
    g.insert_edge(0,3,weight=10)
    
    g.insert_edge(1,3,weight=3)
    g.insert_edge(2,3,weight=1)
    g.insert_edge(3,4,weight=2)

    return g


MAX_WEIGHT = 100

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
    def __init__(self):
        self.verbose = True
        self.directed = False
        self.num_vertices = 0
        self.max_num_vertices = 10
        self.edges = [[] for _ in range(self.max_num_vertices)]
        self.edge_array = []

    def insert_edge(self, x: int, y: int, weight: int = 1) -> None:
        self.edges[x].append(Edge(y, weight))

    def get_root(self) -> int:
        return 1

    def bfs(self, start: int) -> None:
        """
        Performs breadth-first search/traversal (BFS) on the graph
        
        Args:
            start (int): The vertex to start with (Root vertex).
        """
        
        processed = [False] * self.max_num_vertices
        discovered = [False] * self.max_num_vertices
        self.parent = [-1] * self.max_num_vertices
        
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

        self.bfs(self.get_root())

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

        start = 1
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

        print(self.parent)

    def bellman_ford(self, source: int):

        distance = [MAX_WEIGHT] * (self.num_vertices)
        self.parent = [-1] * (self.num_vertices)

        distance[source] = 0

        for _ in range(self.num_vertices-1):
            for v in range(self.num_vertices):
                for edge in self.edges[v]:
                    new_dist = edge.weight + distance[v]
                    if new_dist < distance[edge.v]:
                        distance[edge.v] = new_dist
                        self.parent[edge.v] = v



if __name__ == '__main__':
    g = init_grapth_1(GraphW())
    g.verbose = False


    # g.kruscal()
    # g.prim()
    # g.dijkstra()

    g.bellman_ford(source=0)

    print(g.find_path(6))
