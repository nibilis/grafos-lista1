from src.models2.list_graph import ListGraph
from src.models.undirected_matrix_graph import UndirectedMatrixGraph

class UndirectedListGraph(ListGraph):
    def __init__ (self, nodes):
        super().__init__(nodes)

    def insert_a(self, v, w):
        if w not in self.adjacency_list[v] and v not in self.adjacency_list[w]:
            self.adjacency_list[v].append(w)
            self.adjacency_list[w].append(v)
            self.edges += 1
    
    def remove_a(self, v, w):
        if w in self.adjacency_list[v] and v in self.adjacency_list[w]:
            self.adjacency_list[v].remove(w)
            self.adjacency_list[w].remove(v)
            self.edges -= 1

    def convert_to_matrix(self):
        matrix_graph = UndirectedMatrixGraph(self.nodes)
        matrix_graph.edges = self.edges
        for i in range(self.nodes):
            for j in self.adjacency_list[i]:
                matrix_graph.adjacency_matrix[i][j] = 1
                matrix_graph.adjacency_matrix[j][i] = 1
        return matrix_graph
    
    # Exercicio 29
    def remove_node(self, node):
        if (node >= self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = len(self.adjacency_list[node])

        self.adjacency_list.pop(node)
        for neighbors in self.adjacency_list:
            if node in neighbors:
                neighbors.remove(node)
                removed_edges -= 1
            for i in range(len(neighbors)):
                if neighbors[i] > node:
                    neighbors[i] -= 1

        self.nodes -= 1
        self.edges -= removed_edges
        