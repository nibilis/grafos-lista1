import os
from src.models.list_graph.list_graph import ListGraph

class DirectedListGraph(ListGraph):
    def __init__(self, nodes = 0):
        super().__init__(nodes)

    def insert_a(self, v, w):
        if w not in self.adjacency_list[v]:
            self.adjacency_list[v].append(w)
            self.edges += 1

    def remove_a(self, v, w):
        if w in self.adjacency_list[v]:
            self.adjacency_list[v].remove(w)
            self.edges -= 1

    #exercicio 19
    def inDegree(self, v):
        in_degree = 0
        for i in range(self.nodes):
            if v in self.adjacency_list[i]:
                in_degree += 1
        return in_degree
            
    # Exercicio 20
    def outDegree(self, v):
        return len(self.adjacency_list[v])
    
    # Exercicio 21
    def degree(self, v):
        return self.inDegree(v) + self.outDegree(v)
    
    # Exercicio 23
    def convert_to_matrix(self):
        from src.models.matrix_graph.directed_matrix_graph import DirectedMatrixGraph
        matrix_graph = DirectedMatrixGraph(self.nodes)
        matrix_graph.edges = self.edges
        for i in range(self.nodes):
            for j in self.adjacency_list[i]:
                matrix_graph.adjacency_matrix[i][j] = 1
        return matrix_graph
    
    # Exercicio 28
    def graphFromFile(self, filename):
        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, "..", "..", "tests/resources", filename)
        full_path = os.path.abspath(full_path)

        with open(full_path, "r") as file:
            nodes = int(file.readline())
            if nodes == 0:
                return self

            edges = int(file.readline())
            if edges == 0:
                self.nodes = nodes
                return self

            if edges > nodes ** 2:
                print("Invalid edges quantity")
                return None

            adj_list = [[] for _ in range(nodes)]

            for _ in range(edges):
                origin, destiny = file.readline().split(" ")
                origin = int(origin)
                destiny = int(destiny)
                if origin >= nodes or destiny >= nodes:
                    print(origin + ", " + destiny + " is an invalid edge!")
                    return None
                adj_list[origin].append(destiny)

            self.nodes = nodes
            self.edges = edges
            self.adjacency_list = adj_list
            return self
        
    # Exercicio 30
    def remove_node(self, node):
        if node >= self.nodes:
            print("Invalid node!")
            return
        
        removed_edges = len(self.adjacency_list[node])
        for i in range(self.nodes):
            if node in self.adjacency_list[i]:
                self.adjacency_list[i].remove(node)
                removed_edges += 1

        self.adjacency_list.pop(node)
        self.nodes -= 1
        self.edges -= removed_edges

        for i in range(self.nodes):
            self.adjacency_list[i] = [x-1 if x > node else x for x in self.adjacency_list[i]]

    # Exercicio 31
    def is_complete(self):
        for i in range(self.nodes):
            if len(self.adjacency_list[i]) != self.nodes - 1:
                return False
        return True