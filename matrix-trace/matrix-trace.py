import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    sum = 0
    for i in range(0, len(A)):
        for j in range(0,len(A[i])):
            if(i==j):
                sum = sum + A[i][j]
    return sum
            
    pass
