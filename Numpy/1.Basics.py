# Loading NumPy after installtion
import numpy as np

# The Basics
    ## Array initiallation
    ### Simple Array
a = np.array([1, 2, 3],dtype='int32')
print(a)

    ### 2D array of float
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

    ## Get Dimension of numpy arrays
    ### a.ndim
print(a.ndim)

    ## Get Shape
    ### b.shape
print(b.shape)

    ## Get type
    ###a.dtype
print(a.dtype)

    ##Get Size
    ### a.itemsize
print(a.itemsize)

    ##Get total size
    ### a.nbytes
print(a.nbytes)

    ## Get number of elements 
    ### a,size
print(a.size)


# Accessing/Changing specific elements, rows, columns, etc
