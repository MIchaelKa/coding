import graph_builder as gb

def run_dijkstra():
    g = gb.build_graph_from_file("graph_d_w_1")
    g.dijkstra()
    assert(g.find_path(4)==[0, 2, 3, 4])

    g = gb.build_graph_from_file("graph_d_w_2")
    g.dijkstra()
    assert(g.find_path(6)==[0, 1, 2, 5, 6])

    print("run_dijkstra passed!")

def run_bellman_ford():
    g = gb.build_graph_from_file("graph_d_w_1")
    g.bellman_ford(0)
    assert(g.find_path(4)==[0, 2, 3, 4])

    g = gb.build_graph_from_file("graph_d_w_2")
    g.bellman_ford(0)
    assert(g.find_path(6)==[0, 1, 2, 5, 6])

    print("run_bellman_ford passed!")

def run_tests():
    run_dijkstra()
    run_bellman_ford()

if __name__ == '__main__':
    run_tests()
