import networkx as nx
import numpy as np
import hits

G = nx.gnm_random_graph(80, 160)
G = np.asarray(nx.to_numpy_matrix(G))

h, a = hits.hits(G, steps=10, normalize=True)
#h1, a1 = nx.hits(G)

print(h)
print(a)
#
