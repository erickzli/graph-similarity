import networkx as nx
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from scipy import spatial
import csv

def get_random_capacity_undirected_graph(n, m, max_cap=20):
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
    G = nx.Graph()

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
            G.add_edge(u, v, weight=capa)
            edge_count += 1

    return G

def get_neighbor_edges(G, n):
    '''
    Input a graph and number of nodes
    Return the list of the neighbors of nodes.
    '''
    edge_list = G.edges.data('weight', default=1)
    neighbor = []
    [neighbor.append([]) for i in range(n)]
    # build a node list with adjacent weight edges.
    [(neighbor[edge[0]].append(edge[2]), neighbor[edge[1]].append(edge[2])) for edge in edge_list]

    for i in range(len(neighbor)):
        neighbor[i] = sorted(neighbor[i], reverse=True)

    return neighbor

def closest_node(nl1, nl2):
    '''
    Input two neighbor lists of two graphs
    nl1: the graph as subject
    nl2: the graph as comparable
    Return: list of the closest node list
    '''
    closest_node_list = []
    count = 0
    for i in nl1:
        dist_list = []
        for j in nl2:
            if len(i) == len(j):
                dist_list.append(spatial.distance.euclidean(i, j))
            elif len(i) < len(j):
                [i.append(0) for k in range(len(j)-len(i))]
                dist_list.append(spatial.distance.euclidean(i, j))
            else:
                [j.append(0) for k in range(len(i)-len(j))]
                dist_list.append(spatial.distance.euclidean(i, j))
        closest_node_list.append([count, dist_list.index(min(dist_list))])
        count += 1
    return closest_node_list



n = 20
m = 40
mcap = 5

G1 = get_random_capacity_undirected_graph(n, m, max_cap=mcap)
G2 = get_random_capacity_undirected_graph(n, m, max_cap=mcap)

neighbor1 = get_neighbor_edges(G1, n)
neighbor2 = get_neighbor_edges(G2, n)

cnl1 = closest_node(neighbor1, neighbor2)
cnl2 = closest_node(neighbor2, neighbor1)

best_neighbor_list = []
for i in range(len(cnl1)):
    if cnl1[i][0] == cnl2[cnl1[i][1]][1]:
        best_neighbor_list.append([cnl1[i][0], cnl1[i][1]])

print('G1->G2, neighbor', cnl1)
print('\n')
print('G2->G1, neighbor', cnl2)
print('\n')
print('G1->G2, mutual neighbor', best_neighbor_list)
print('\n')

myFile = open('closest_neighbor.csv', 'w+')
myFile.write('Nodes in G1,Closest neighbor in G2\n')
[myFile.write(str(i) + ',' + str(cnl1[i]) + '\n') for i in range(len(cnl1))]
myFile.write('Nodes in G1,Closest neighbor in G2\n')
[myFile.write(str(i) + ',' + str(cnl2[i]) + '\n') for i in range(len(cnl2))]
myFile.write('Nodes in G1,Best neighbor in G2\n')
[myFile.write(str(i[0]) + ',' + str(i[1]) + '\n') for i in best_neighbor_list]

myFile.close()

pos = nx.circular_layout(G1)
edges = G1.edges()
weights = [G1[u][v]['weight'] for u,v in edges]
weights[:] = [x / (mcap / 10.0) for x in weights]
nx.draw(G1, pos, edges=edges, width=weights, with_labels=True)
plt.savefig('G1.png')

pos = nx.circular_layout(G2)
edges = G2.edges()
weights = [G2[u][v]['weight'] for u,v in edges]
weights[:] = [x / (mcap / 10.0) for x in weights]
nx.draw(G2, pos, edges=edges, width=weights, with_labels=True)
plt.savefig('G2.png')
