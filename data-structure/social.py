import networkx as nx
import matplotlib.pyplot as plt

class SocialMediaNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_user(self, user):
        # Add a user (node) to the social media network
        self.graph.add_node(user)

    def add_relationship(self, from_user, to_user, relationship_type):
        # Add a relationship (edge) between two users
        self.graph.add_edge(from_user, to_user, relationship=relationship_type)

    def find_connections(self, user):
        # Find all connections (friends) of a user
        connections = []
        for neighbor in self.graph.neighbors(user):
            relationship_type = self.graph[user][neighbor]["relationship"]
            connections.append((neighbor, relationship_type))
        return connections

    def analyze_social_circles(self):
        # Analyze social circles within the network
        circles = list(nx.connected_components(self.graph))
        return circles

    def recommend_connections(self, user):
        # Recommend new connections based on common interests (shared connections)
        recommendations = []
        for neighbor in self.graph.neighbors(user):
            for potential_connection in self.graph.neighbors(neighbor):
                if potential_connection != user and not self.graph.has_edge(user, potential_connection):
                    recommendations.append((potential_connection, "Potential Connection"))
        return recommendations

    def visualize(self):
        # Visualize the social media network
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.graph, 'relationship')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

# Create a social media network instance
social_media_network = SocialMediaNetwork()

# Add users to the network
users_relationships = [
    ("David", "Eve", "Friend"),
    ("Frank", "Grace", "Colleague"),
    ("Harry", "Ivy", "Family"),
    ("Frank", "Eve", "Colleague"),
    ("Jack", "Kelly", "Friend"),
    ("Liam", "Mia", "Colleague"),
    ("Nathan", "Olivia", "Friend"),
    ("Peter", "Quinn", "Family"),
    ("Peter", "Sam", "Family"),
    ("Rachel", "Sam", "Colleague"),
    ("Jack", "Ulysses", "Friend"),
    ("Tina", "Ulysses", "Friend"),
    ("Violet", "Walter", "Family"),
    ("Xena", "Yvonne", "Friend"),
]

for from_user, to_user, relationship_type in users_relationships:
    social_media_network.add_user(from_user)
    social_media_network.add_user(to_user)
    social_media_network.add_relationship(from_user, to_user, relationship_type)

# Find connections for each user
for user in set(u for u, _, _ in users_relationships):
    connections = social_media_network.find_connections(user)
    print(f"Connections for {user}: {connections}")

# Analyze social circles for each user
for user in set(u for u, _, _ in users_relationships):
    social_circles = social_media_network.analyze_social_circles()
    user_social_circle = [circle for circle in social_circles if user in circle]
    print(f"Social Circles for {user}: {user_social_circle if user_social_circle else 0}")

# Recommend connections for each user
for user in set(u for u, _, _ in users_relationships):
    recommendations = social_media_network.recommend_connections(user)
    print(f"Recommendations for {user}: {recommendations}")

# Visualize the social media network
social_media_network.visualize()
