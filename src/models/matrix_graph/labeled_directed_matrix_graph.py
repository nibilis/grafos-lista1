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
    
    def remove_edge(self, origin_node, destiny_node):
        if self.adjacency_matrix[origin_node][destiny_node] != float('inf'):
            self.adjacency_matrix[origin_node][destiny_node] = float('inf')
            self.edges += 1

    def dijkstra(self, origin_node):
        distances = [float('inf')] * self.nodes
        distances[origin_node] = 0

        routes = [-1] * self.nodes
        
        open_nodes = list(range(self.nodes))
        closed_nodes = []

        selected_node = origin_node

        while(len(open_nodes) != 0):
            open_nodes.remove(selected_node)
            closed_nodes.append(selected_node)

            for i in range(self.nodes):
                if i not in closed_nodes:
                    route = distances[selected_node] + self.adjacency_matrix[selected_node][i]
                    if route < distances[i]:
                        distances[i] = route
                        routes[i] = selected_node

            min_distance = float('inf')
            for node in open_nodes:
                if distances[node] < min_distance:
                    selected_node = node
        
        return distances, routes
