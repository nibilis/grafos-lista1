from src.models.directed_matrix_graph import DirectedMatrixGraph

def test_directed_matrix_graph():
    g = DirectedMatrixGraph(4)

    g.insert_a(0,1)
    g.insert_a(0,2)
    g.insert_a(2,1)
    g.insert_a(2,3)
    g.insert_a(1,3)

    g.show()
    g.show_min()

    vertice_exemplo = 0
    print(f"Grau de entrada do vértice {vertice_exemplo} = {g.in_degree(0)}")
    print(f"Grau de saída do vértice {vertice_exemplo} = {g.out_degree(0)}")
    print("Grau do vértice", vertice_exemplo, "=" , g.degree(0))
    print("Vértice", vertice_exemplo, "é fonte: " , g.is_source(0))
    print("Vértice", vertice_exemplo, "é sorvedouro: " , g.is_sink(0))
    print("Grafo é simétrico: ", g.is_simetric())

    file_name = "input_graph.txt"

    input_graph = DirectedMatrixGraph()
    input_graph = input_graph.graph_from_file(file_name)
    input_graph.show_min()

    input_graph.remove_node(2)
    input_graph.show_min()

    print("Grafo do arquivo é completo:", input_graph.is_complete())

    print("Grafo é fortemente conexo:", input_graph.fconexo())

    g2 = DirectedMatrixGraph(3)
    g2.insert_a(0, 1)
    g2.insert_a(1, 2)
    g2.insert_a(2, 0)

    print("Grafo g2 tem o grau de conexidade: ", g2.conexidade())

    g2.convert_to_list().show()

    

if __name__ == "__main__":
    test_directed_matrix_graph()
