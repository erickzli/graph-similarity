import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import datetime

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
        t1 = datetime.datetime.now()
        authorityA, hubA = hits(a, steps, normalize)
        authorityB, hubB = hits(b, steps, normalize)
        t2 = datetime.datetime.now()
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

def effe(start, end, step, printTimes=True, plot=True):
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


def hits(a, steps, normalize):
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
