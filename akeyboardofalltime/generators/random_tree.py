#! python3
import networkx as nx
import string
import random
import sys

seed = int(sys.argv[1])
word_len = int(sys.argv[2])

random.seed(seed)

# generating graph
G: nx.Graph = nx.random_spanning_tree(nx.complete_graph(26))

mapping = {coord: idx for idx, coord in enumerate(G.nodes())}
G = nx.relabel_nodes(G, mapping)

# generating word
alphabet = string.ascii_uppercase
word = "".join(random.choices(alphabet, k=word_len))

# label size, nodecount, edgecount
print(G.number_of_nodes(), G.number_of_edges())

# adjacency list
for node, neighbor in G.edges:
    print(f"{alphabet[node]} {alphabet[neighbor]}")

a, b = random.sample(list(word), 2)
print(a, b)
print(word)
