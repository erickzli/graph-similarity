import hits
import networkx as nx

G = hits.get_random_capacity_graph(100, 200, max_cap=50, directed=True)
# G = nx.gnm_random_graph(10, 20)

score, dictt = hits.get_max_flow(G, 3, 70)

print(score)
