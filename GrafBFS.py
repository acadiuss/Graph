import matplotlib.pyplot as plt
import networkx as nx
from queue import Queue

# Przykładowy graf

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 4, 'D': 3, 'E': 4},
    'C': {'A': 1, 'F': 5},
    'D': {'B': 3},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 5, 'E': 1}
}
graph2= {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
graph3 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    'E': ['F'],
    'F': ['E']
}


# Definicja funkcji BFS
def bfs(graph, start, end):
    queue = Queue()
    queue.put((start, [start]))
    visited = set()

    while not queue.empty():
        vertex, path = queue.get()

        if vertex not in visited:
            visited.add(vertex)

            if vertex == end:
                return path

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.put((neighbor, path + [neighbor]))

    return None

path = bfs(graph, 'A', 'F')
G = nx.Graph(graph)

# Rysowanie
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=700, font_size=8)

# Zaznaczanie krawędzi 
edges_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges_path, edge_color='red', width=2)

# Dodanie etykiet dla krawędzi na ścieżce
edge_labels = {(path[i], path[i + 1]): i + 1 for i in range(len(path) - 1)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Wyświetlenie rysunku
plt.show()
