import hits
import networkx as nx
from collections import OrderedDict
from scipy import spatial

graph_num = 10

h_list = []
a_list = []
mf_list = []


for i in range(graph_num):
    G = hits.get_random_capacity_graph(10, 20, max_cap=30, max_wei=10)

    h, a = nx.hits(G)
    h = [(k,v) for v,k in sorted([(v,k) for k,v in h.items()])]
    a = [(k,v) for v,k in sorted([(v,k) for k,v in a.items()])]
    mf = hits.get_max_flow_score(G, 3, 8)

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

print(len(mf_dist_list))
