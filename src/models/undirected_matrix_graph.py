from collections import deque
from src.models.matrix_graph import MatrixGraph 

class UndirectedMatrixGraph(MatrixGraph):
    def __init__(self, nodes = 0):
        super().__init__(nodes)
        self.adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]

    # Exercicio 8
    def insert_edge(self, v, w):
        if self.adjacency_matrix[v][w] == 0:
            self.adjacency_matrix[v][w] = 1
            self.adjacency_matrix[w][v] = 1
            self.edges += 1

    def remove_a(self, v, w):
        if self.adjacency_matrix[v][w] == 1:
            self.adjacency_matrix[v][w] = 0
            self.adjacency_matrix[w][v] = 0
            self.edges -= 1
    
    # Exercicio 9
    def degree(self, node):
        degree = 0
        for edge in range(self.nodes):
            if (self.adjacency_matrix[node][edge]):
                degree += 1
        return degree
    
    # Exercicio 11
    def remove_node(self, node):
        if (node > self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = sum(self.adjacency_matrix[node])

        self.adjacency_matrix.pop(node)
        for row in self.adjacency_matrix:
            row.pop(node)

        self.nodes -= 1
        self.edges -= removed_edges
    
    # Exercicio 15
    def is_connected(self):
        visited = [False] * self.nodes
        queue = deque([0])
        visited[0] = True

        while queue:
            u = queue.popleft()
            for v in range(self.nodes):
                if self.adjacency_matrix[u][v] != 0 and not visited[v]:
                    visited[v] = True
                    queue.append(v)

        if all(visited):
            return 0
        return 1