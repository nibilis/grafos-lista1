class MatrixGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = 0
        self.adjacency_matrix = [[None for i in range(nodes)] for j in range(nodes)]

    def show(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(f"Adj[{i:2d},{j:2d}] =", self.adjacency_matrix[i][j], "", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    
    def show_min(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for w in range(self.nodes):
                print("", self.adjacency_matrix[i][w], "", end="") 
            print("\n")
        print("\nfim da impressao do grafo." )

    # Exercicio 11
    def remove_node(self, node):
        if (node > self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = sum(self.adjacency_matrix[node])
        removed_edges += sum(row[node] for row in self.adjacency_matrix)

        self.adjacency_matrix.pop(node)
        for row in self.adjacency_matrix:
            row.pop(node)

        self.nodes -= 1
        self.edges -= removed_edges

    # Exercicios 12 e 13
    def is_complete(self):
        for i in range(self.nodes):
            for j in range(self.nodes):
                if(self.adjacency_matrix[i][j] != 0):
                    return False
        return True
    
    # Exercicio 14
    def complementary_graph(self):
        complementary_graph = MatrixGraph(self.nodes)
    
        for i in range(self.nodes):
            for j in range(self.nodes):
                if(self.adjacency_matrix[i][j] == 0):
                    complementary_graph.adjacency_matrix[i][j] = 1
                    continue
                complementary_graph.adjacency_matrix[i][j] = 0

        return complementary_graph
    
    # Exercicio 23
    def convert_to_list(self):
        from src.models2.list_graph import ListGraph
        list_graph = ListGraph(self.nodes)
        list_graph.edges = self.edges
        for i in range(self.nodes):
            for j in range(self.nodes):
                if self.adjacency_matrix[i][j] == 1:
                    list_graph.adjacency_list[i].append(j)
        return list_graph

    