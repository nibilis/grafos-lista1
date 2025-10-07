from src.models.matrix_graph.labeled_undirected_matrix_graph import LabeledUndirectedMatrixGraph 

def test_labeled_undirected_matrix_graph():
    graph = LabeledUndirectedMatrixGraph(10)
    graph.insert_edge(0, 1, 4)
    graph.insert_edge(0, 2, 8)
    graph.insert_edge(1, 2, 11)
    graph.insert_edge(1, 3, 8)
    graph.insert_edge(2, 4, 7)
    graph.insert_edge(3, 4, 2)
    graph.insert_edge(3, 5, 7)
    graph.insert_edge(4, 6, 9)
    graph.insert_edge(5, 6, 4)
    graph.insert_edge(5, 7, 14)
    graph.insert_edge(6, 7, 10)
    graph.insert_edge(7, 8, 2)
    graph.insert_edge(8, 9, 1)
    graph.insert_edge(7, 9, 6)

    print("Algoritmo de Kruskal:")

    graph.kruskal()

    print("Algoritmo de Prim:")
    graph.prim()

if __name__ == "__main__":
    test_labeled_undirected_matrix_graph()