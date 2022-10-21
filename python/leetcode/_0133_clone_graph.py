from __future__ import annotations
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
class GraphBuilder:
    def __init__(self):
        self.nodes = {}
        
    def get_node(self, i: int) -> Node:
        if i in self.nodes:
            return self.nodes[i]
        else:
            node = Node(val=i)
            self.nodes[i] = node
            return node
        
    def init_graph_from_adj_list(self, adj_list: list[list[int]]) -> Node:
        self.nodes = {}
        
        for i, v_list in enumerate(adj_list):
            node = self.get_node(i+1)
            for v in v_list:
                node.neighbors.append(self.get_node(v))
        return self.nodes[1]
    
    def clone(self, root: Node):
        self.nodes = {}
        
        queue = deque()
        discovered = {}

        discovered[root.val] = True
        queue.append(root)
        
        while queue:
            node = queue.popleft() 
            new_node = self.get_node(node.val)
            
            for n in node.neighbors:
                new_n = self.get_node(n.val)
                new_node.neighbors.append(new_n)
                if n.val not in discovered:
                    queue.append(n)
                    discovered[n.val] = True
                    
        return self.nodes[root.val]
        

def process_node(node: Node):
    print(f"process_node: {node.val}")
    
def bfs(root: Node):
    
    queue = deque()
    discovered = {}
    
    discovered[root.val] = True
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        process_node(node)
        for n in node.neighbors:
            if n.val not in discovered:
                queue.append(n)
                discovered[n.val] = True
            