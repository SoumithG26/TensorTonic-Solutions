import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a2 = np.linalg.norm(a)
    b2 = np.linalg.norm(b)
    res = np.dot(a,b)/np.linalg.norm(a2*b2)
    if np.linalg.norm(a2*b2)==0:
        return 0
    else:
        return res
    pass