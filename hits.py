import numpy as np

def hits(a, k=10):
    '''
    Use HITS algorithm to find the authority and hub scores for each vertix.

    Parameters
    ----------
    a: a numpy matrix of vertices relation
    k: number of steps, default == 40

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
        authorityScore = np.dot(aT, hubScore)
        authorityScore = normalization(authorityScore)

        hubScore = np.dot(a, authorityScore)
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

    denominator = 0.0

    for i in score:
        denominator += (i ** 2)
        #print(i)

    denominator = denominator ** 0.5

    score = score / denominator

    return score
