import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    p = np.array(x)
    q = np.array(y)
    dist = np.sqrt(np.sum((p - q)**2))
    return dist
    pass