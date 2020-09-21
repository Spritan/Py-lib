# Loading NumPy after installtion
import numpy as np

# Accessing/Changing specific elements, rows, columns, etc
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Get a specific element [r, c]
a[1, 5]

# Get a specific row
a[0, :]

# Get a specific column
a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]


a[1, 5] = 20

a[:, 2] = [1, 2]
print(a)

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

# Get specific element (work outside in)
b[0, 1, 1]

# replace
b[:, 1, :] = [[9, 9, 9], [8, 8]]

"""
    ---------------------------------------------------------------------------
    ValueError                                Traceback(most recent call last)
    <ipython-input-34-db1aebb5daad > in < module > ()
    1  # replace
    --- -> 2 b[:, 1, :] = [[9, 9, 9], [8, 8]]

    ValueError: setting an array element with a sequence.
"""

b
