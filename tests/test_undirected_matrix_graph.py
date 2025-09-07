from src.models.matrix_graph.undirected_matrix_graph import UndirectedMatrixGraph

def test_undirected_matrix_graph():
    graph = UndirectedMatrixGraph(4)

    graph.insert_edge(0,1)
    graph.insert_edge(0,2)
    graph.insert_edge(2,1)
    graph.insert_edge(2,3)
    graph.insert_edge(1,3)
    print("Exercicio 8: ")
    graph.show_min()

    print("Exercicio 9: Grau do vértice 0: ", graph.degree(0))

    print("Exercicio 11: ")
    graph.remove_node(2)
    graph.show_min()
    
    print("Exercicio 12: Grafo é completo:", graph.is_complete())

    complementary_graph = graph.complementary_graph()
    print("Exercicio 14: Grafo complementar:")
    complementary_graph.show_min()

    print("Exercício 15: Grafo é conexo:", graph.is_connected())

if __name__ == "__main__":
    test_undirected_matrix_graph()