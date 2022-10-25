from __future__ import annotations
from collections import deque

from union_set import UnionSet

def init_grapth_1(g: GraphW) -> GraphW:
    g.num_vertices = 7

    g.insert_edge(1,2,weight=5)
    g.insert_edge(1,3,weight=7)
    g.insert_edge(1,4,weight=12)
    
    
    g.insert_edge(2,1,weight=5)
    g.insert_edge(2,3,weight=9)
    g.insert_edge(2,5,weight=7)

    g.insert_edge(3,1,weight=7)
    g.insert_edge(3,2,weight=9)
    g.insert_edge(3,5,weight=4)
    g.insert_edge(3,6,weight=3)
    g.insert_edge(3,4,weight=4)

    g.insert_edge(4,1,weight=12)
    g.insert_edge(4,3,weight=4)
    g.insert_edge(4,6,weight=7)
    
    g.insert_edge(5,2,weight=7)
    g.insert_edge(5,3,weight=4)
    g.insert_edge(5,6,weight=2)
    g.insert_edge(5,7,weight=5)

    g.insert_edge(6,3,weight=3)
    g.insert_edge(6,4,weight=7)
    g.insert_edge(6,5,weight=2)
    g.insert_edge(6,7,weight=2)

    g.insert_edge(7,5,weight=5)
    g.insert_edge(7,6,weight=2)
    
    return g

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

        union_set = UnionSet(self.num_vertices+1)

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

        intree = [False] * (self.num_vertices + 1)
        distance = [100] * (self.num_vertices + 1)
        parent = [-1] * (self.num_vertices + 1)

        v = 1

        # stops when we will not able to update v
        while not intree[v]:

            intree[v] = True

            for edge in self.edges[v]:
                if edge.weight < distance[edge.v] and not intree[edge.v]:
                    distance[edge.v] = edge.weight
                    parent[edge.v] = v
            
            
            # select min dist from distance array and add this vertex
            # чтобы проверить этот массив все равно совершаем О(n) операций ?!
            dist = 100
            for i in range(self.num_vertices):
                if not intree[i] and distance[i] < dist:
                    dist = distance[i]
                    v = i

            # TODO: prints the last edge two tipes
            print(v)

        print(parent)

    def find_path(self, v: int, parent: list[int]) -> list[int]:

        if parent[v] == -1:
            return [v]

        path = self.find_path(parent[v], parent)
        path.append(v)
        return path


if __name__ == '__main__':
    g = init_grapth_1(GraphW())
    g.verbose = False


    # g.kruscal()

    g.prim()
