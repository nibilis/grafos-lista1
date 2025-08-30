from src.models.labeled_directed_matrix_graph import LabeledDirectedMatrixGraph

def test_labeled_directed_matrix_graph():
    graph = LabeledDirectedMatrixGraph(4)

    graph.insert_edge(0, 1, 10)
    graph.insert_edge(0, 2, 7)
    graph.insert_edge(2, 1, 8)
    graph.insert_edge(2, 3, 5)
    graph.insert_edge(1, 3, 4)

    graph.show()
    graph.show_min()

if __name__ == "__main__":
    test_labeled_directed_matrix_graph()