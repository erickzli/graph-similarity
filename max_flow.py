import hits
import networkx as nx

nodes = 100
edges = 200
scores = []

G = hits.get_random_capacity_graph(nodes, edges, max_cap=50, directed=True)
h, a = nx.hits(G, max_iter=100)
print('hub scores: ', h)
print('authority scores: ', a)

for i in range(nodes-1):
    for j in range(i+1, nodes):
        scores.append(hits.get_max_flow_score(G, i, j))

print('Max score: ', max(scores)})
print('Average score: ', sum(scores) / float(len(scores)))
