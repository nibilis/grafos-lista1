from src.models.matrix_graph.labeled_directed_matrix_graph import LabeledDirectedMatrixGraph

def test_dijkstra():
    graph1 = LabeledDirectedMatrixGraph(5)

    graph1.insert_edge(0, 1, 1)
    graph1.insert_edge(0, 4, 1)

    graph1.insert_edge(1, 2, 1)
    graph1.insert_edge(1, 3, 2)

    graph1.insert_edge(2, 3, 4)
    graph1.insert_edge(2, 4, 2)

    graph1.insert_edge(3, 0, 3)
    
    graph1.insert_edge(4, 0, 2)
    graph1.insert_edge(4, 3, 1)

    distances, routes = graph1.dijkstra(0)
    print("graph1 distances array:", distances)
    print("graph1 routes array:", routes)


    graph2 = LabeledDirectedMatrixGraph(4)

    graph2.insert_edge(0, 0, 0)
    graph2.insert_edge(0, 1, 20)
    graph2.insert_edge(0, 2, 30)
    graph2.insert_edge(0, 3, 50)

    graph2.insert_edge(1, 0, 20)
    graph2.insert_edge(1, 0, 0)
    graph2.insert_edge(1, 2, 40)
    graph2.insert_edge(1, 3, 15)

    graph2.insert_edge(2, 0, 30)
    graph2.insert_edge(2, 1, 40)
    graph2.insert_edge(2, 0, 0)
    graph2.insert_edge(2, 3, 15)

    graph2.insert_edge(3, 0, 50)
    graph2.insert_edge(3, 1, 15)
    graph2.insert_edge(3, 2, 15)
    graph2.insert_edge(3, 0, 0)

    distances, routes = graph2.dijkstra(2)
    print("graph2 distances array:", distances)
    print("graph2 routes array:", routes)

if __name__ == "__main__":
    test_dijkstra()