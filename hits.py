import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
from scipy import spatial

def comparison(a, b, steps=40, normalize=True, lapse=False):
    '''
    Compare two graphs whether they are similar.
    Print out the scores and indicate whether they are similar.

    Parameters
    ----------
    a: a numpy array of graph A
    b: a numpy array of graph B
    steps: number of steps; default: 40
    normalize: determine whether the scores should be normalized; default: True
    lapse: determine the time lapsed during a function call; default: False

    '''

    t1 = 0.0
    t2 = 0.0
    uptime = 0.0
    # Obviously, if the dimensions of the two graphs are different, they cannot
    #  be similar...
    if np.size(a) != np.size(b):
        print('They should have had the same size')
        return

    if lapse:
        t1 = time.time()
        authorityA, hubA = hits(a, steps, normalize)
        authorityB, hubB = hits(b, steps, normalize)
        t2 = time.time()
        uptime = t2 - t1
    else:
        authorityA, hubA = hits(a, steps, normalize)
        authorityB, hubB = hits(b, steps, normalize)

    authorityA = np.sort(authorityA)
    authorityB = np.sort(authorityB)

    hubA = np.sort(hubA)
    hubB = np.sort(hubB)

    # With tolerance, since the same numbers can be calculated with error by
    #  using different approaches.
    authorityEqual = np.allclose(authorityA, authorityB)
    hubEqual = np.allclose(hubA, hubB)

    print('Authority score for A are {0} with {1} step(s)'.format(authorityA, steps))
    print('Hub score for A are {0} with {1} step(s)'.format(hubA, steps))

    print('Authority score for B are {0} with {1} step(s)'.format(authorityB, steps))
    print('Hub score for B are {0} with {1} step(s)'.format(hubB, steps))

    if authorityEqual and hubEqual:
        print('Similar!!')
    else:
        print('Different')

    if lapse:
        return uptime
    else:
        return


def efficiency(start, end, step, printTimes=True, plot=True):
    '''
    calculate time used for different nodes in graphs using HITS algorithm.
    '''
    n = []
    t = []

    for loop in range(start, end+1, step):
        G = nx.gnm_random_graph(loop, loop*2)
        G = np.asarray(nx.to_numpy_matrix(G))

        t1 = datetime.datetime.now()
        garb1, garb2 = hits.hits(G, steps=50, normalize=True)
        t2 = datetime.datetime.now()
        uptime = t2 - t1
        uptime = uptime.microseconds

        if loop != start:
            n.append(loop)
            t.append(uptime)

        if printTimes:
            print('{0} nodes utilized {1} ms'.format(loop, uptime))

    if plot:
        plt.plot(n, t)
        plt.title('Time difference among # of nodes')
        plt.xlabel('Number of nodes')
        plt.ylabel('Time used')
        plt.show()



def random_distance(nodes, edges, sampleSize=100, sortBy='authority', distType='Manhattan'):
    '''
    create random graphs and get the distance between the sample and base

    Parameters
    ----------
    nodes: number of nodes
    edges: number of edges
    sampleSize: size of samples; default=100
    sortBy: the score that is used for sorting; default='authority'
    distType: type of distance used for dist calculation;
                default='Manhattan'

    '''
    if (not isinstance(nodes, int)) or (not isinstance(edges, int)):
        exit('Error: Not both nodes and edges are integers.')

    if nodes < 5:
        exit('Error: nodes are too few.')

    if edges < nodes:
        exit('Error: edges are fewer than nodes.')

    auth_list = []
    hub_list = []

    base_list = []
    samples_list = []

    distances_list = []
    topFiveDist_list = []

    G = nx.gnm_random_graph(nodes, edges)
    G = np.asarray(nx.to_numpy_matrix(G))
    auth, hub = hits(G)

    for i in range(sampleSize):
        Gi = nx.gnm_random_graph(nodes, edges)
        Gi = np.asarray(nx.to_numpy_matrix(Gi))
        authi, hubi = hits(Gi)

        auth_list.append(authi)
        hub_list.append(hubi)

    # sort by which index
    if sortBy == 'authority':
        base_list = np.sort(auth)
        for i in range(sampleSize):
            samples_list.append(np.sort(auth_list[i]))
    else:
        base_list = np.sort(hub)
        for i in range(sampleSize):
            samples_list.append(np.sort(hub_list[i]))

    for i in range(sampleSize):
        if distType == 'Manhattan':
            distances_list.append(spatial.distance.cityblock(base_list, samples_list[i]))
        elif distType == 'Euclidean':
            distances_list.append(spatial.distance.euclidean(base_list, samples_list[i]))
        elif distType == 'Chebyshev':
            distances_list.append(spatial.distance.chebyshev(base_list, samples_list[i]))
        else:
            distances_list.append(spatial.distance.cosine(base_list, samples_list[i]))

    return distances_list


def hits(a, steps=100, normalize=True):
    '''
    Use HITS algorithm to find the authority and hub scores for each vertix.

    Parameters
    ----------
    a: a numpy matrix of vertices relation
    steps: number of steps
    normalize: determine whether the scores should be normalized

    Return
    ------
    the numpy array of authority scores and hub scores

    '''

    # Get the number of vertices in this graph
    numOfVertices = int(np.size(a) ** 0.5)
    aT = np.transpose(a)

    authorityScore = np.ones(numOfVertices, dtype=np.float64)
    hubScore = np.ones(numOfVertices, dtype=np.float64)

    for i in range(steps):
        # update the authority scores, and then normalize them
        authorityScore = np.dot(a, hubScore)
        if normalize:
            authorityScore = normalization(authorityScore)

        # update the hub scores, and then normalize them
        hubScore = np.dot(a, authorityScore)
        if normalize:
            hubScore = normalization(hubScore)

    return authorityScore, hubScore


def normalization(score):
    '''
    Get the normalized score vector

    Parameter
    ---------
    score: a numpy array of authority or hub scores

    Return
    ------
    a numpy array of normalized score vector

    '''

    # the factor used for normalization
    denominator = 0.0
    for i in score:
        denominator += (i ** 2.0)

    denominator = denominator ** 0.5
    score = score / denominator

    return score


def get_random_capacity_graph(n, m, max_cap=10, directed=False):
    """
    Returns a `G_{n,m}` random graph.

    In the `G_{n,m}` model, a graph is chosen uniformly at random from the set
    of all graphs with `n` nodes and `m` edges.

    This algorithm should be faster than :func:`dense_gnm_random_graph` for
    sparse graphs.

    Parameters
    ----------
    n : int
        The number of nodes.
    m : int
        The number of edges.
    seed : int, optional
        Seed for random number generator (default=None).
    directed : bool, optional (default=False)
        If True return a directed graph

    """
    if directed:
        G=nx.DiGraph()
    else:
        G=nx.Graph()
    G.add_nodes_from(range(n))
    G.name="gnm_random_graph(%s,%s)"%(n,m)

    if n==1:
        return G
    max_edges=n*(n-1)
    if not directed:
        max_edges/=2.0
    if m>=max_edges:
        return complete_graph(n,create_using=G)

    nlist=list(G.nodes())
    edge_count=0

    print(nlist)

    while edge_count < m:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)

        if u==v or G.has_edge(u,v):
            continue
        else:
            capa = random.randint(1, max_cap)
            G.add_edge(u, v, capacity=capa)
            # G.add_edge(u, v)
            edge_count=edge_count+1

    return G


def get_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)
