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
    result = g.bellman_ford(0)
    assert(result == True)
    assert(g.find_path(4)==[0, 2, 3, 4])

    g = gb.build_graph_from_file("graph_d_w_2")
    result = g.bellman_ford(0)
    assert(result == True)
    assert(g.find_path(6)==[0, 1, 2, 5, 6])

    g = gb.build_graph_from_file("graph_d_w_3_nc")
    result = g.bellman_ford(0)
    assert(result == False)

    # Cormen [22.1-6]
    g = gb.build_graph_from_file("graph_d_w_4")
    result = g.bellman_ford_min_paths()
    assert(result == True)
    assert(g.distance==[100, -4, 2, -10, -5])

    print("run_bellman_ford passed!")

def run_tests():
    run_dijkstra()
    run_bellman_ford()

if __name__ == '__main__':
    run_tests()
