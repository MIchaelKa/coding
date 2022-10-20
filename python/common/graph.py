from __future__ import annotations
from collections import defaultdict, deque

# TODO: write a func to validate graph
def init_grapth_1():
    g = Graph()

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

def init_grapth_2():
    g = Graph()

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

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.directed = False
        
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
        self.num_edges = 0
        
        # num_vertices = len(self.edges.keys())
        num_vertices = 10
        
        processed = [False] * num_vertices
        discovered = [False] * num_vertices
        self.parent = [-1] * num_vertices
        
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
        print(f"process_vertex_early: {vertex}")
    
    def process_vertex_late(self, vertex: int) -> None:
        print(f"process_vertex_late: {vertex}")
        print("")
    
    def process_edge(self, x: int, y: int) -> None:
        print(f"process_edge: {x}-{y}")

        # BFS: counting edges
        # self.num_edges += 1

        # DFS: detecting cycles
        if self.parent[y] != x:
            print("cycle detected")

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
        # num_vertices = len(self.edges.keys())
        num_vertices = 10

        self.parent = [-1] * num_vertices
        self.discovered = [False] * num_vertices
        self.processed = [False] * num_vertices
        self.entry_time = [-1] * num_vertices
        self.exit_time = [-1] * num_vertices

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
                self.process_edge(v, y)
                self.dfs_helper(y)
            elif not self.processed[y] and self.parent[v] != y: # TODO: add check self.directed 
                # Can we tell this is a back edge?
                self.process_edge(v, y)

        self.process_vertex_late(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True

if __name__ == '__main__':
    g = init_grapth_2()
    # g.bfs(g.get_root())
    g.dfs(g.get_root())
    print(g.parent)
    print(g.entry_time)
    print(g.exit_time)