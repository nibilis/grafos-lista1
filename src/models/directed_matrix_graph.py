import os

class DirectedMatrixGraph:
    def __init__(self, nodes = 0):
        self.nodes = nodes
        self.edges = 0
        self.adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]

    # Exercicio 7
    def graph_from_file(self, filename):
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

            adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

            for _ in range(edges):
                origin, destiny = file.readline().split(" ")
                origin = int(origin)
                destiny = int(destiny)
                if origin >= nodes or destiny >= nodes:
                    print(origin + ", " + destiny + " is an invalid edge!")
                    return None
                adj_matrix[origin][destiny] = 1

            self.nodes = nodes
            self.edges = edges
            self.adjacency_matrix = adj_matrix
            return self
                    

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insert_a(self, v, w):
        if self.adjacency_matrix[v][w] == 0:
            self.adjacency_matrix[v][w] = 1
            self.edges+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def remove_a(self, v, w):
        # testa se temos a aresta
        if self.adjacency_matrix[v][w] == 1:
            self.adjacency_matrix[v][w] = 0
            self.edges-=1

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for w in range(self.nodes):
                if self.adjacency_matrix[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def show_min(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for w in range(self.nodes):
                if self.adjacency_matrix[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    
    # Exercicio 1
    def in_degree(self, v):
        in_degree = 0
        for aresta in range(self.nodes):
            if self.adjacency_matrix[aresta][v] == 1:
                in_degree += 1
        return in_degree
    
    # Exercicio 2
    def out_degree(self, v):
        out_degree = 0
        for aresta in range(self.nodes):
            if self.adjacency_matrix[v][aresta] == 1:
                out_degree += 1
        return out_degree
    
    # Exercicio 3
    def degree(self, v): 
        return self.in_degree(v) + self.out_degree(v)
    
    # Exercicio 4
    def is_source(self, v):
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return True
        return False
    
    # Exercicio 5
    def is_sink(self, v):
        if self.in_degree(v) > 0 and self.out_degree(v) == 0:
            return True
        return False
    
    # Exercicio 6
    def is_simetric(self):
        for i in range(self.nodes):
            for j in range(self.nodes - i):
                if self.adjacency_matrix[i][j] != self.adjacency_matrix[j][i]:
                    return False
        return True
    
