import os
import graph_w as gw

def build_graph_from_file(file_name: str) -> gw.GraphW:

    cwd = os.getcwd()

    file_path = os.path.join(cwd, "resources", f"{file_name}.txt")

    with open(file_path) as file:
        lines = [line.rstrip('\n') for line in file]
        directed = bool(lines[0]=="true")
        num_vertices = int(lines[1])

        g = gw.GraphW(directed, num_vertices)

        for i in range(2, len(lines)):
            edge = [int(x) for x in lines[i].rstrip().split(',')]
            g.insert_edge(edge[0],edge[1],edge[2])

    
    return g
