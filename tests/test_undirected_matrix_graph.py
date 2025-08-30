from src.models.undirected_matrix_graph import UndirectedMatrixGraph

def test_undirected_matrix_graph():
    graph = UndirectedMatrixGraph(4)

    graph.insert_edge(0,1)
    graph.insert_edge(0,2)
    graph.insert_edge(2,1)
    graph.insert_edge(2,3)
    graph.insert_edge(1,3)
    graph.show_min()

    graph.remove_node(2)
    graph.show_min()

    print("Grafo é completo:", graph.is_complete())

    complementary_graph = graph.complementary_graph()
    print("Grafo complementar:")
    complementary_graph.show_min()

    print("Grafo é conexo:", graph.is_connected())

if __name__ == "__main__":
    test_undirected_matrix_graph()