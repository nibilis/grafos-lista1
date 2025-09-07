from src.models2.directed_list_graph import DirectedListGraph

def test_directed_list_graph():
    g = DirectedListGraph(4)

    g.insert_a(0,1)
    g.insert_a(0,2)
    g.insert_a(2,1)
    g.insert_a(2,3)

    g.show()

    print("In-Degree of 1:", g.inDegree(1))  # Expected: 2
    print("Out-Degree of 2:", g.outDegree(2))  # Expected: 2

    g2 = DirectedListGraph(4)

    g2.insert_a(0,1)
    g2.insert_a(0,2)
    g2.insert_a(2,1)
    g2.insert_a(2,3)

    print("Graphs are equal:", g.is_equal(g2))  # Expected: True

    g2.convert_to_matrix().show_min()

    g2.show()

    is_source = g2.is_source(0)
    print("Vertex 0 is a source:", is_source)  # Expected: True
    is_source = g2.is_source(1)
    print("Vertex 1 is a source:", is_source)  # Expected: False
    is_sink = g2.is_sink(3)
    print("Vertex 3 is a sink:", is_sink)  # Expected: True

    print("Graph g2 is symmetric:", g2.is_simetric())  # Expected: False

    g3 = DirectedListGraph(4)
    g3.insert_a(0,1)
    g3.insert_a(1,0)
    g3.insert_a(0,3)
    g3.insert_a(3,0)
    g3.insert_a(1,2)
    g3.insert_a(2,1)
    g3.insert_a(2,3)
    g3.insert_a(3,2)
    print("Graph g3 is symmetric:", g3.is_simetric())  # Expected: True

    print("Before 2 is removed: ")
    g3.show()
    g3.remove_node(2)
    print("After 2 is removed: ")
    g3.show()

    gfile = DirectedListGraph()
    gfile = gfile.graphFromFile("input_graph.txt")
    gfile.show()

if __name__ == "__main__":
    test_directed_list_graph()