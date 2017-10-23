import numpy as np

def comparison(a, b):
    authorityA, hubA = hits(a)
    authorityB, hubB = hits(b)

    authorityA = np.sort(authorityA)
    authorityB = np.sort(authorityB)

    hubA = np.sort(hubA)
    hubB = np.sort(hubB)

def hits(a, k=40, normalize=True):
    '''
    Use HITS algorithm to find the authority and hub scores for each vertix.

    Parameters
    ----------
    a: a numpy matrix of vertices relation
    k: number of steps, default: 40 steps
    normalize: determine whether the scores should be normalized, default: True

    Return
    ------
    the numpy array of authority scores and hub scores
    '''

    # Get the number of vertices in this graph
    numOfVertices = int(np.size(a) ** 0.5)
    aT = np.transpose(a)

    authorityScore = np.ones(numOfVertices, dtype=np.float64)
    hubScore = np.ones(numOfVertices, dtype=np.float64)

    for i in range(k):
        # update the authority scores, and then normalize them
        authorityScore = np.dot(aT, hubScore)
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
        denominator += (i ** 2)

    denominator = denominator ** 0.5
    score = score / denominator

    return score
