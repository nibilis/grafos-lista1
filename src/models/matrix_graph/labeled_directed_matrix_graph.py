from src.models.matrix_graph.matrix_graph import MatrixGraph 

class LabeledDirectedMatrixGraph(MatrixGraph):
    def __init__(self, nodes = 0):
        super().__init__(nodes)
        self.adjacency_matrix = [[float('inf') for i in range(nodes)] for j in range(nodes)]

    # Exercicio 10 e 18
    def insert_edge(self, origin_node, destiny_node, label):
        if self.adjacency_matrix[origin_node][destiny_node] == float('inf'):
            self.adjacency_matrix[origin_node][destiny_node] = label
            self.edges += 1
    
    def remove_edge(self, origin_node, destiny_node, label):
        if self.adjacency_matrix[origin_node][destiny_node] != float('inf'):
            self.adjacency_matrix[origin_node][destiny_node] = float('inf')
            self.edges += 1