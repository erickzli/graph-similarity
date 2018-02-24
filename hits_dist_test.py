import hits
import matplotlib.pyplot as plt
import numpy as np

maxnode = 300
dist_list = []
nodes = np.arange(maxnode-10)
nodes = nodes + 10

for i in range(10,maxnode):
    dist = hits.random_distance(i,2*i)
    dist_mean = np.mean(dist)
    dist_list.append(dist_mean)
    print('finish: ', i)

print(dist_list)

plt.scatter(nodes, dist_list)
plt.xlabel('number of nodes')
plt.ylabel('average manhattan distance')
plt.show()
