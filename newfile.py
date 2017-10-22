import hits
import numpy as np

a = np.array([[0., 1., 1., 1.], [0., 0., 1., 1.], [1., 0., 0., 1.], [0., 0., 0., 1.]])

ascore = 0.0
hscore = 0.0

ascore, hscore = hits.hits(a, 40)

print(ascore)
print(hscore)
