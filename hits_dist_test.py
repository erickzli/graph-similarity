import hits
import matplotlib.pyplot as plt
import numpy as np

start = 10
maxnode = 1000
step = 10
dist_list = []
nodes = np.arange(start, maxnode, step)

for i in range(start, maxnode, step):
    dist = hits.random_distance(i,2*i)
    dist_mean = np.mean(dist)
    dist_list.append(dist_mean)
    print('finish: ', i)

print(dist_list)

plt.scatter(nodes, dist_list)
plt.xlabel('number of nodes')
plt.ylabel('average manhattan distance')
plt.show()
