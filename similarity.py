import hits
import numpy as np

''' Two similar graphs with different indices'''
a = np.array([[0., 1., 1., 0.], \
              [0., 0., 0., 0.], \
              [0., 1., 0., 1.], \
              [1., 1., 0., 1.]])

# b = np.array([[0., 1., 1., 0.], \
#               [0., 0., 0., 0.], \
#               [0., 1., 0., 1.], \
#               [1., 1., 0., 1.]])

b = np.array(([[1., 1., 1., 0.], \
               [0., 0., 1., 1.], \
               [0., 0., 0., 0.], \
               [1., 0., 1., 0.]]))

# ascoreA = 0.0
# hscoreA = 0.0
# step = 40
# normalize = True
#
# ascoreA, hscoreA = hits.hits(a, step, normalize)
#
# ascoreB = 0.0
# hscoreB = 0.0
# # step = 1
# # normalize = True
#
# ascoreB, hscoreB = hits.hits(b, step, normalize)

# print('Authority score for A are {0} with {1} step(s)'.format(ascoreA, step))
# print('Hub score for A are {0} with {1} step(s)'.format(hscoreA, step))
#
# print('Authority score for B are {0} with {1} step(s)'.format(ascoreB, step))
# print('Hub score for B are {0} with {1} step(s)'.format(hscoreB, step))

hits.comparison(a, b)
