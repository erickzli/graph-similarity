import hits
import numpy as np

a = np.array([[0., 1., 1., 1.], \
              [0., 0., 1., 1.], \
              [1., 0., 0., 1.], \
              [0., 0., 0., 1.]])

ascore = 0.0
hscore = 0.0
step = 1
normalize = True

ascore, hscore = hits.hits(a, step, normalize)

print('Authority score are {0} with {1} step(s)'.format(ascore, step))
print('Hub score are {0} with {1} step(s)'.format(hscore, step))
