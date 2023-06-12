import networkx as nx
import matplotlib.pyplot as plt
import itertools

# Create a dictionary to map city names to city indices
city_names = {}
num_cities = int(input("Enter the number of cities: "))
for i in range(num_cities):
    city_name = input(f"Enter the name of city {i+1}: ")
    city_names[city_name] = i

# Take the city distances as input from the user
city_distances = []
print("Enter the distances between the cities:")
for i in range(num_cities):
    row = input(f"Enter the distances from {list(city_names.keys())[i]} to all other cities: ").split()
    city_distances.append([int(d) for d in row])

# Create a weighted graph using NetworkX
G = nx.Graph()
for i in range(num_cities):
    for j in range(i+1, num_cities):
        G.add_edge(list(city_names.keys())[i], list(city_names.keys())[j], weight=city_distances[i][j])

# Find all possible permutations of the cities
city_permutations = list(itertools.permutations(list(city_names.keys())))

# Compute the total distance of each permutation and find the minimum
min_distance = float('inf')
min_path = None
for path in city_permutations:
    distance = sum([city_distances[city_names[path[i-1]]][city_names[path[i]]] for i in range(num_cities)])
    if distance < min_distance:
        min_distance = distance
        min_path = path

# Highlight the chosen path by changing the color and width of the edges
edges = list(zip(min_path[:-1], min_path[1:]))
edge_colors = ['r' if e in edges or e[::-1] in edges else 'k' for e in G.edges()]
edge_widths = [2 if e in edges or e[::-1] in edges else 1 for e in G.edges()]

# Draw the graph with the optimal path highlighted and edge weights shown
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='b')
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw_networkx_labels(G, pos, font_size=16, font_color='w')
plt.axis('off')
plt.show()