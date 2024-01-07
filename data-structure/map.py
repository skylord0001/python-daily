import heapq
import matplotlib.pyplot as plt
import networkx as nx
import json

class Graph:
    def __init__(self):
        # Initialize an empty set for nodes and an empty dictionary for edges
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        # Add a node to the graph
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        # Add an edge with a specified weight between two nodes
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, start, end):
        # Dijkstra's algorithm to find the shortest path between two nodes
        min_heap = [(0, start, [])]
        visited = set()

        while min_heap:
            (current_cost, current_node, path) = heapq.heappop(min_heap)

            if current_node not in visited:
                visited.add(current_node)
                path = path + [current_node]

                if current_node == end:
                    return (current_cost, path)

                for neighbor, weight in self.edges[current_node]:
                    heapq.heappush(min_heap, (current_cost + weight, neighbor, path))

        return float('inf'), []

    def visualize(self):
        # Visualize the graph using NetworkX and Matplotlib
        G = nx.Graph()

        for node in self.nodes:
            G.add_node(node)

        for node, neighbors in self.edges.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        labels = {node: node for node in G.nodes()}

        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

# Load JSON data
json_data = '''
{
  "nodes": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
  "edges": [
    {"from": "A", "to": "B", "weight": 2},
    {"from": "A", "to": "C", "weight": 4},
    {"from": "B", "to": "D", "weight": 7},
    {"from": "C", "to": "D", "weight": 1},
    {"from": "B", "to": "E", "weight": 3},
    {"from": "C", "to": "F", "weight": 5},
    {"from": "D", "to": "G", "weight": 6},
    {"from": "E", "to": "H", "weight": 2},
    {"from": "F", "to": "I", "weight": 3},
    {"from": "G", "to": "J", "weight": 4},
    {"from": "H", "to": "K", "weight": 5},
    {"from": "I", "to": "L", "weight": 2},
    {"from": "J", "to": "L", "weight": 6},
    {"from": "K", "to": "L", "weight": 3}
  ]
}
'''

# Convert JSON to Python dictionary
graph_data = json.loads(json_data)

# Create Graph instance and populate it with nodes and edges
map_graph = Graph()
for node in graph_data["nodes"]:
    map_graph.add_node(node)

for edge in graph_data["edges"]:
    map_graph.add_edge(edge["from"], edge["to"], edge["weight"])


# Find the fastest route from "A" to "L"
shortest_distance, shortest_path = map_graph.dijkstra("A", "L")

print(f"Shortest Distance: {shortest_distance}")
print(f"Shortest Path: {shortest_path}")


# Visualize the graph
map_graph.visualize()