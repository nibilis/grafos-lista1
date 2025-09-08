import os
from src.models.matrix_graph.matrix_graph import MatrixGraph

class DirectedMatrixGraph(MatrixGraph):
    def __init__(self, nodes = 0):
        super().__init__(nodes)
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
    
    def reduce_graph(self):
        all_scc = []
        remaining_nodes = set(range(self.nodes))
        while remaining_nodes:
            node = remaining_nodes.pop()
            scc = set(self.transitivoDireto(node)).intersection(set(self.transitivoInverso(node)))
            all_scc.append(scc)
            remaining_nodes.difference_update(scc)
        
        reduced = DirectedMatrixGraph(len(all_scc))
        for i in range(len(all_scc)):
            for j in range(len(all_scc)):
                if i != j:
                    for v in all_scc[i]:
                        for w in all_scc[j]:
                            if self.adjacency_matrix[v][w] == 1:
                                reduced.insert_a(i, j)
                                break
                        else:
                            continue
                        break

        return reduced

    # Exercicio 16
    def conexidade(self):
        categoria = "C3"
        if not self.grafoFconexo():
            categoria = "C2"
            if not self.sfconexo():
                categoria = "C0"
                if not self.desconexo():
                    categoria = "C1"
        return categoria
            
    def grafoFconexo(self):
        return self.fconexo(0)

    def fconexo(self, node):
        if self.in_degree(node) == 0 or self.out_degree(node) == 0:
            return False
        
        #inicia em um vertice qualquer
        #encontrar todos os vertices atingiveis a partir dele
        direto = self.transitivoDireto(node) #ao final, direto terá todos os vertices atingiveis a partir do vertice 0
        indireto = self.transitivoInverso(node) #ao final, indireto terá todos os vertices que atingem o vertice 0
        for i in range(self.nodes):
            if len(direto) != self.nodes or len(indireto) != self.nodes:
                return False
        return True

    def sfconexo(self):
        y = []
        for i in range(self.nodes):
            direto = self.transitivoDireto(i)
            indireto = self.transitivoInverso(i)
            w = list(set(direto).union(set(indireto))) # R+(i) U R-(i)
            if len(w) != self.nodes:
                return False
            else:
                if len(direto) == self.nodes or len(indireto) == self.nodes:
                    y.append(i)
                else:
                    return False
        if len(y) == self.nodes:
            return True
        return False
    
    def desconexo(self):
        for i in range(self.nodes):
            w = list(set(self.transitivoDireto(i)).union(set(self.transitivoInverso(i))))
            if len(w) == self.nodes:
                return False
        return True
                
        
    def transitivoDireto(self, v):
        visited = [False] * self.nodes
        visited[v] = True
        atingiveis = [v]
        self._transitivoDireto(v, visited, atingiveis)
        return atingiveis
    
    def _transitivoDireto(self, v, visited, atingiveis):
        for i in range(self.nodes):
            if self.adjacency_matrix[v][i] == 1 and not visited[i]:
                visited[i] = True
                atingiveis.append(i)
                self._transitivoDireto(i, visited, atingiveis)

    def transitivoInverso(self, v):
        visited = [False] * self.nodes
        visited[v] = True
        atingiveis = [v]
        self._transitivoInverso(v, visited, atingiveis)
        return atingiveis
    
    def _transitivoInverso(self, v, visited, atingiveis):
        for i in range(self.nodes):
            if self.adjacency_matrix[i][v] == 1 and not visited[i]:
                visited[i] = True
                atingiveis.append(i)
                self._transitivoInverso(i, visited, atingiveis)
    
    