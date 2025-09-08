from src.models.matrix_graph.directed_matrix_graph import DirectedMatrixGraph

def test_directed_matrix_graph():
    g3 = DirectedMatrixGraph(8)
    g3.insert_a(0, 1)
    g3.insert_a(0, 2)
    g3.insert_a(1, 3)
    g3.insert_a(1, 5)
    g3.insert_a(2, 3)
    g3.insert_a(3, 2)
    g3.insert_a(4, 0)
    g3.insert_a(4, 1)
    g3.insert_a(5, 4)
    g3.insert_a(6, 4)
    g3.insert_a(6, 7)
    g3.insert_a(7, 5)
    g3.insert_a(7, 6)

    print("Grafo original:")
    g3.show_min()
    print("\nGrafo reduzido:")
    g3.reduce_graph().show_min()
    

if __name__ == "__main__":
    test_directed_matrix_graph()
