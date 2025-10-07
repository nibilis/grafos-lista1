from collections import deque
from src.models.matrix_graph.matrix_graph import MatrixGraph 

class LabeledUndirectedMatrixGraph(MatrixGraph):
    def __init__(self, nodes):
        super().__init__(nodes)
        self.adjacency_matrix = [[float('inf') for i in range(nodes)] for j in range(nodes)]
    
    def insert_edge(self, v, w, label):
        if self.adjacency_matrix[v][w] == float('inf'):
            self.adjacency_matrix[v][w] = label
            self.adjacency_matrix[w][v] = label
            self.edges += 1
    
    def remove_edge(self, v, w):
        if self.adjacency_matrix[v][w] != float('inf'):
            self.adjacency_matrix[v][w] = float('inf')
            self.adjacency_matrix[w][v] = float('inf')
            self.edges -= 1
    
    def degree(self, node):
        degree = 0
        for edge in range(self.nodes):
            if (self.adjacency_matrix[node][edge] != float('inf')):
                degree += 1
        return degree
    
    def remove_node(self, node):
        if (node > self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = 0
        for edge in self.adjacency_matrix[node]:
            if edge != float('inf'):
                removed_edges += 1

        self.adjacency_matrix.pop(node)
        for row in self.adjacency_matrix:
            row.pop(node)

        self.nodes -= 1
        self.edges -= removed_edges

    def is_connected(self):
        visited = [False] * self.nodes
        queue = deque([0])
        visited[0] = True

        while queue:
            u = queue.popleft()
            for v in range(self.nodes):
                if self.adjacency_matrix[u][v] != float('inf') and not visited[v]:
                    visited[v] = True
                    queue.append(v)

        if all(visited):
            return True
        return False
    

    def kruskal(self):
        if not self.is_connected():
            print("Grafo nao conexo. Impossivel aplicar o algoritmo de Kruskal.")
            return
        if self.edges <= 1:
            print("Grafo com 1 ou menos arestas. Impossivel aplicar o algoritmo de Kruskal.")
            return
        v = []  
        k = 0
        t = 0
        bigT = []
        custoMinimo = 0
        for i in range(self.nodes):
            v.append(i)
        ordenada = self.ordenacao(self.adjacency_matrix, self.nodes)
        while t < self.nodes - 1:
            i = ordenada[k][0] 
            j = ordenada[k][1] 
            k += 1
            if v[i] != v[j]:
                val = max(v[i], v[j])
                for cont in range(self.nodes):
                    if v[cont] == val:
                        v[cont] = min(v[i], v[j])
                bigT.append((i, j))
                custoMinimo += self.adjacency_matrix[i][j]
                t += 1
        
        for i in range(len(bigT)):
            if bigT[i] != []:
                print(f"{i+1}a: {bigT[i]}")
        print("Custo minimo: ", custoMinimo)
    
    def ordenacao(self, matriz, n):
        ordenada = []
        for i in range(n):
            for j in range(i, n):
                if matriz[i][j] != float('inf'):
                    ordenada.append((i, j, matriz[i][j]))
        ordenada.sort(key=lambda x: x[2])
        return ordenada

    def prim(self):
        if not self.is_connected():
            print("Grafo nao conexo. Impossivel aplicar o algoritmo de Prim.")
            return
        if self.edges <= 1:
            print("Grafo com 1 ou menos arestas. Impossivel aplicar o algoritmo de Prim.")
            return
        valor = float('inf')
        custo = 0
        bigT = [0]
        bigE = []
        self._prim(bigT, bigE, valor, custo)
    
    def _prim(self, bigT, bigE, valor, custo):

        for k in range(len(bigT)):
            for i in range(self.nodes):
                if(i not in bigT):
                    if(self.adjacency_matrix[bigT[k]][i] < valor):
                        valor = self.adjacency_matrix[bigT[k]][i]
                        vint = bigT[k]
                        vext = i
        custo += valor
        bigT.append(vext)
        bigE.append((vint, vext))
        valor = float('inf')
        if(len(bigT) < self.nodes):
            self._prim(bigT, bigE, valor, custo)
        else:
            for i in range(len(bigE)):
                print(f"{i+1}a: {bigE[i]}")
            print("Custo minimo: ", custo)