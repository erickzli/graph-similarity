import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import datetime
import hits

def effe(start, end, printTimes=True, plot=True):
    n = []
    t = []

    for loop in range(start, end+1):
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
            print('{0} nodes utilized {1}'.format(loop, uptime))

    if plot:
        plt.plot(n, t)
        plt.title('Time difference among # of nodes')
        plt.xlabel('Number of nodes')
        plt.ylabel('Time used')
        plt.show()


effe(5, 1000)
