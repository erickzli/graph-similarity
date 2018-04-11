import hits
import random
import networkx as nx
from collections import OrderedDict
from scipy import spatial
import matplotlib.pyplot as plt
import numpy.random as npr


def get_random_capacity_directed_graph(n, m, max_cap=20):
    '''
    Returns a `G_{n,m}` random directed graph with capacity.

    In the `G_{n,m}` model, a graph is chosen uniformly at random from the set
    of all graphs with `n` nodes and `m` edges.

    Partial credit to NetworkX.

    Parameters
    ----------
    n : int
        The number of nodes.
    m : int
        The number of edges.
    max_cap : int, optional
        Maximum capacity allowed for every edge (default=20).

    '''
    G = nx.DiGraph()

    G.add_nodes_from(range(n))
    G.name = "gnm_random_graph(%s,%s)"%(n, m)

    if n == 1:
        return
    max_edges = n * (n - 1)
    if m >= max_edges:
        return complete_graph(n, create_using=G)

    nlist = list(G.nodes())
    edge_count = 0

    while edge_count < m:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)

        if u == v or G.has_edge(u, v):
            continue
        else:
            capa = random.randint(1, max_cap)
            G.add_edge(u, v, capacity=capa)
            edge_count += 1

    return G


graph_num = 100
nodes = 20
edges = 40
cap = 15

h_list = []
a_list = []
mf_list = []

for i in range(graph_num):
    G = get_random_capacity_directed_graph(nodes, edges, max_cap=cap)

    h, a = nx.hits(G)
    h = [(k,v) for v,k in sorted([(v,k) for k,v in h.items()])]
    a = [(k,v) for v,k in sorted([(v,k) for k,v in a.items()])]

    source = npr.randint(0, high=nodes)
    sink = npr.randint(0, high=nodes)
    while sink == source:
        sink = npr.randint(0, high=nodes)

    mf = hits.get_max_flow_score(G, source, sink)

    h_n = []
    a_n = []
    for item in h:
        h_n.append(item[1])
    for item in a:
        a_n.append(item[1])

    h_list.append(h_n)
    a_list.append(a_n)
    mf_list.append(mf)

h_dist_list = []
a_dist_list = []
mf_dist_list = []

for i in range(graph_num-1):
    for j in range(i+1, graph_num):
        h_dist_list.append(spatial.distance.cityblock(h_list[i], h_list[j]))
        a_dist_list.append(spatial.distance.cityblock(a_list[i], a_list[j]))
        mf_dist_list.append(abs(mf_list[i] - mf_list[j]))

plt.subplot(1, 2, 1)
plt.scatter(h_dist_list, mf_dist_list, marker='o', color='red')
plt.xlabel('distance of hub scores')
plt.ylabel('distance of max flow scores')
plt.title('Dist of hub vs dist of max flow')


plt.subplot(1, 2, 2)
plt.scatter(a_dist_list, mf_dist_list, marker='^', color='blue')
plt.xlabel('distance of authority scores')
plt.title('Dist of authority vs dist of max flow')

plt.suptitle(f'{graph_num} graphs with {nodes} nodes and {edges} edges, max capacity={cap}', fontsize=12)

plt.show()
