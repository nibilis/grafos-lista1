class ListGraph():
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = 0
        self.adjacency_list = [[] for _ in range(nodes)]
    
    def show(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            print(f"{i} -> ", end="")
            for j in range(len(self.adjacency_list[i])):
                print(f"{self.adjacency_list[i][j]} -> ", end="")
            print("None")

    # Exercicio 22
    def is_equal(self, other):
        if self.nodes != other.nodes or self.edges != other.edges:
            return False
        for i in range(self.nodes):
            if sorted(self.adjacency_list[i]) != sorted(other.adjacency_list[i]):
                return False
        return True
    
    # Exercicio 23
    def convert_to_matrix(self):
        from src.models.matrix_graph.matrix_graph import MatrixGraph
        matrix_graph = MatrixGraph(self.nodes)
        matrix_graph.edges = self.edges
        for i in range(self.nodes):
            for j in self.adjacency_list[i]:
                matrix_graph.adjacency_matrix[i][j] = 1
        return matrix_graph
    
    # Exercicio 25
    def is_source(self, v):
        if self.inDegree(v) < self.outDegree(v):
            return True
        return False
    
    # Exercicio 26
    def is_sink(self, v):
        if self.inDegree(v) > 0 and self.outDegree(v) == 0:
            return True
        return False
    
    # Exercicio 27
    def is_simetric(self):
        for i in range(self.nodes):
            for j in range(self.nodes):
                if i in self.adjacency_list[j] and j not in self.adjacency_list[i]:
                    return False
        return True
    


    # Exercicio 24
    def invert_list(self):
        inverted_graph = ListGraph(self.nodes)
        inverted_graph.edges = self.edges
        for i in range(self.nodes):
            for v in reversed(self.adjacency_list[i]):
                inverted_graph.adjacency_list[i].append(v)
        return inverted_graph

        