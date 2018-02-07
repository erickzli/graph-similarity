import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import hits

n = 100
m = 200
plot = True
# generate a random graph with n nodes and m edges.
G1 = nx.gnm_random_graph(n, m)
G2 = nx.gnm_random_graph(n, m)

A = np.asarray(nx.to_numpy_matrix(G1))
B = np.asarray(nx.to_numpy_matrix(G2))

hits.comparison(A, B, steps=50, normalize=True)

if plot:
    plt.subplot(121)
    nx.draw(G2, with_labels=True, font_weight='bold')
    plt.show()
