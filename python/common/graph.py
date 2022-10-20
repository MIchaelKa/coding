from __future__ import annotations
from collections import defaultdict, deque

# TODO: write a func to validate graph
def init_grapth_1(g: Graph) -> Graph:
    g.insert_edge(1,7)
    g.insert_edge(1,2)
    
    g.insert_edge(1,8)
    
    g.insert_edge(2,1)
    g.insert_edge(2,3)
    g.insert_edge(2,7)
    g.insert_edge(2,5)

    g.insert_edge(3,2)

    g.insert_edge(5,2)

    g.insert_edge(7,1)
    g.insert_edge(7,2)

    g.insert_edge(8,1)
    
    return g

def init_grapth_2(g: Graph) -> Graph:
    g.insert_edge(1,2)
    g.insert_edge(1,7)
    g.insert_edge(1,8)
    
    g.insert_edge(2,1)
    g.insert_edge(2,3)
    g.insert_edge(2,5)
    g.insert_edge(2,7)
    
    g.insert_edge(3,2)
    g.insert_edge(3,4)
    g.insert_edge(3,5)

    g.insert_edge(4,3)
    g.insert_edge(4,5)

    g.insert_edge(5,2)
    g.insert_edge(5,3)
    g.insert_edge(5,4)
    g.insert_edge(5,6)

    g.insert_edge(6,5)

    g.insert_edge(7,1)
    g.insert_edge(7,2)

    g.insert_edge(8,1)
    
    return g

from enum import Enum

class Edge(Enum):
    TREE = 1
    BACK = 2
    FORWARD = 3
    CROSS = 4

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.directed = False

        # num_vertices = len(self.edges.keys())
        self.max_num_vertices = 10

        self.verbose = True
        
    def insert_edge(self, x: int, y: int) -> None:
        self.edges[x].append(y)
        
    def print(self) -> None:
        for vert, edges in self.edges.items():
            print(f'vertex: {vert:2d}')
            print(f'edges : ', end='')
            for edge in edges:
                print(f'{edge:2d} ', end='')
            print('')
            
    def get_root(self) -> int:
        return list(self.edges.keys())[0]
            
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
            
            for y in vertex_edges:
                if not processed[y] or self.directed:
                    self.process_edge(vertex, y)
                
                if not discovered[y]:
                    queue.append(y)
                    discovered[y] = True
                    self.parent[y] = vertex
                    
            self.process_vertex_late(vertex)
        
    def process_vertex_early(self, vertex: int) -> None:
        if self.verbose:
            print(f"process_vertex_early: {vertex}")
    
    def process_vertex_late(self, vertex: int) -> None:
        if self.verbose:
            print(f"process_vertex_late: {vertex}\n")
    
    def process_edge(self, x: int, y: int) -> None:
        if self.verbose:
            print(f"process_edge: {x}-{y}")

    def find_path(self, start: int, end: int) -> list[int]:
        """
        Finds a shortest path from start vertex to end vertex.
        It's only valid if BFS was performed with start as a root of search.
        
        Args:
            start (int): The vertex to start with
            end (int): The end vertex

        Returns:
            list[int]: List of vertecies which represent the path
        """
        if start == end:
            return [start]
        
        path = self.find_path(start, self.parent[end])
        path.append(end)
        return path
    

    def dfs(self, start: int) -> None:
        self.parent = [-1] * self.max_num_vertices
        self.discovered = [False] * self.max_num_vertices
        self.processed = [False] * self.max_num_vertices
        self.entry_time = [-1] * self.max_num_vertices
        self.exit_time = [-1] * self.max_num_vertices

        self.time = 0

        self.dfs_helper(start)


    def dfs_helper(self, v: int) -> None:

        self.discovered[v] = True
        
        self.time += 1
        self.entry_time[v] = self.time

        self.process_vertex_early(v)

        vertex_edges = self.edges[v] # will it speed it up?
        for y in vertex_edges:
            if not self.discovered[y]:
                self.parent[y] = v
                self.process_edge(v, y) # Edge.TREE
                self.dfs_helper(y)
            elif not self.processed[y] and self.parent[v] != y: # TODO: add check self.directed 
                self.process_edge(v, y) # Can we tell this is Edge.BACK?

        self.process_vertex_late(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True

    def edge_classification(self, x: int, y: int) -> Edge:
        """
        Should be called from process_edge method
        """

        # проверяем родителя вершины назначения
        if self.parent[y] == x:
            return Edge.TREE
        
        # проверка вершины отправления
        # self.parent[x] == y
        # Если это родитель проверяемой вершины - мы не должны обрабатывать
        # такое ребро, так как это будет во второй раз
        # такой ситуации не должно быть в этом методе
        # self.parent[x] != y всегда в этом месте
        
        if self.discovered[y] and not self.processed[y]: # Do we really need self.processed[y] check for DFS?
            return Edge.BACK


#
# GraphCountEdges
# 

class GraphCountEdges(Graph):
    def __init__(self):
        super().__init__()
        self.num_edges = 0

    def process_edge(self, x: int, y: int) -> None:
        super().process_edge(x, y)
        self.num_edges += 1

def count_edges():
    g = init_grapth_2(GraphCountEdges)
    
    g.bfs(g.get_root())
    # g.dfs(g.get_root()) # also works

    print(g.num_edges)

#
# GraphCycleDetector
# 

class GraphCycleDetector(Graph):
    def process_edge(self, x: int, y: int) -> None:
        super().process_edge(x, y)
        if self.parent[y] != x:
            print("cycle detected")

def detect_cycles():
    g = init_grapth_2(GraphCycleDetector)
    g.dfs(g.get_root())


#
# GraphArticulationVDetector
# 

class GraphArticulationVDetector(Graph):
    def __init__(self):
        super().__init__()
        self.reachable_ancestor = [-1] * self.max_num_vertices # most reachable
        self.tree_out_degree = [0] * self.max_num_vertices # количество листьев
        self.verbose = False

    def process_vertex_early(self, vertex: int) -> None:
        super().process_vertex_early(vertex)
        self.reachable_ancestor[vertex] = vertex

    def process_vertex_late(self, vertex: int) -> None:

        if self.parent[vertex] == -1: # root
            if self.tree_out_degree[vertex] > 1:
                print(f"root articulation vertex: {vertex} ")
            return

        if self.parent[self.parent[vertex]] != -1: # if parent is not root

            if self.reachable_ancestor[vertex] == self.parent[vertex]:
                print(f"parent articulation vertex: {self.parent[vertex]} ")

            if self.reachable_ancestor[vertex] == vertex:
                print(f"bridge articulation vertex - parent: {self.parent[vertex]} ")

                if self.tree_out_degree[vertex] > 0:
                    print(f"bridge articulation vertex - self: {vertex} ")

        time_vertex = self.entry_time[self.reachable_ancestor[vertex]]
        time_parent = self.entry_time[self.reachable_ancestor[self.parent[vertex]]]

        if time_vertex < time_parent:
            self.reachable_ancestor[self.parent[vertex]] = self.reachable_ancestor[vertex]
            if self.verbose:
                print(f"update parent reachable ancestor: {self.parent[vertex]} <- {vertex} : {self.reachable_ancestor[vertex]}")

        super().process_vertex_late(vertex)

    def process_edge(self, x: int, y: int) -> None:
        super().process_edge(x, y)
        
        edge = self.edge_classification(x, y)

        if edge == Edge.TREE:
            self.tree_out_degree[x] += 1

        if edge == Edge.BACK: # and parent[x] != y должно уже выполняться
            if self.entry_time[y] < self.entry_time[self.reachable_ancestor[x]]:
                    self.reachable_ancestor[x] = y

        if self.verbose:
            print(edge)

def articulation_vertices():
    g = init_grapth_2(GraphArticulationVDetector())
    g.dfs(g.get_root())

    print(g.parent)
    print(g.entry_time)
    print(g.exit_time)

if __name__ == '__main__':
    articulation_vertices()

