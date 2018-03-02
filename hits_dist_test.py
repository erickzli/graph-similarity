import hits
import matplotlib.pyplot as plt
import numpy as np

start = 10
maxnode = 1000
step = 10
dist_type = 'Manhattan'
sort_by = 'hub'
sample_size = 100
edge_to_node = 3


mean_list = []
median_list = []
max_list = []
min_list = []
nodes = np.arange(start, maxnode, step)

for i in range(start, maxnode, step):
    dist = hits.random_distance(i, edge_to_node*i, sampleSize=sample_size, sortBy=sort_by, distType=dist_type)
    mean_list.append(np.mean(dist))
    median_list.append(np.median(dist))
    max_list.append(np.amax(dist))
    min_list.append(np.amin(dist))
    print('finish: ', i)

f, axarr = plt.subplots(2, 2, sharex='col', sharey='row')
axarr[0, 0].scatter(nodes, mean_list)
axarr[0, 0].set_title('Mean')
axarr[0, 1].scatter(nodes, median_list)
axarr[0, 1].set_title('Median')
axarr[1, 0].scatter(nodes, max_list)
axarr[1, 0].set_title('Max')
axarr[1, 1].scatter(nodes, min_list)
axarr[1, 1].set_title('Min')
for ax in axarr.flat:
    ax.set(xlabel='Number of nodes', ylabel='Distance')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axarr.flat:
    ax.label_outer()

plt.suptitle(f'{dist_type} distance sorted by {sort_by} with {sample_size} samples and {edge_to_node} edges per node')
plt.show()
