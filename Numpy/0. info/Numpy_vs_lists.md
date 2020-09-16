# Python Lists VS Numpy Arrays

**NumPy** is the fundamental package for scientific computing in Python. [NumPy](https://www.geeksforgeeks.org/python-numpy/) arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences. NumPy is not another programming language but a Python extension module. It provides fast and efficient operations on arrays of homogeneous data.

**Some important points about Numpy arrays:**

- We can create a N-dimensional array in python using numpy.array().
- Array are by default Homogeneous, which means data inside an array must be of the same Datatype. (Note you can also create a structured array in python).
- Element wise operation is possible.
- Numpy array has the various function, methods, and variables, to ease our task of matrix computation.
- Elements of an array are stored contiguously in memory. For example, all rows of a two dimensioned array must have the same number of columns. Or a three dimensioned array must have the same number of rows and columns on each card.

**Representation of Numpy array:**

- Single Dimensional Numpy Array;

  *filter_none*

  *edit*

  *play_arrow*

  *brightness_4*

  `import` `numpy as np `` ` `a ``=` `np.array([``1``, ``2``, ``3``]) ``print``(a) `

  **Output:**

  ```
  [1 2 3]
  ```

- Multi-dimensional Numpy Array:

  *filter_none*

  *edit*

  *play_arrow*

  *brightness_4*

  `import` `numpy as np `` ` `a ``=` `np.array([(``1``, ``2``, ``3``), (``4``, ``5``, ``6``)]) ``print``(a) `

  **Output:**

  

  ```
  [[1 2 3]
   [4 5 6]]
  ```

**Advantages of using Numpy Arrays Over Python Lists:**

- consumes less memory.
- fast as compared to the python List.
- convenient to use.

**List:** A [list](https://www.geeksforgeeks.org/python-list/) is a collection which is ordered and changeable. In Python, lists are written with square brackets.

**Some important points about Python Lists:**

- The list can be homogeneous or heterogeneous.
- Element wise operation is not possible on the list.
- Python list is by default 1 dimensional. But we can create an N-Dimensional list. But then too it will be 1 D list storing another 1D list
- Elements of a list need not be contiguous in memory.

Below are some examples which clearly demonstrate how Numpy arrays are better than Python lists by analyzing the memory consumption, execution time comparison, and operations supported by both of them.

**Example 1: Memory consumption between Numpy array and lists**
In this example, a Python list and a Numpy array of size 1000 will be created. The size of each element and then the whole size of both the containers will be calculated and comparison will be done in terms of memory consumption.

Below is the implementation.

*filter_none*

*edit*

*play_arrow*

*brightness_4*

```
# importing numpy package ``import` `numpy as np `` ` `# importing system module ``import` `sys `` ` `# declaring a list of 1000 elements ``S``=` `range``(``1000``) `` ` `# printing size of each element of the list ``print``(``"Size of each element of list in bytes: "``,sys.getsizeof(S)) `` ` `# printing size of the whole list ``print``(``"Size of the whole list in bytes: "``,sys.getsizeof(S)``*``len``(S)) `` ` `# declaring a Numpy array of 1000 elements ``D``=` `np.arange(``1000``) `` ` `# printing size of each element of the Numpy array ``print``(``"Size of each element of the Numpy array in bytes: "``,D.itemsize) `` ` `# printing size of the whole Numpy array ``print``(``"Size of the whole Numpy array in bytes: "``,D.size``*``D.itemsize) 
```

**Output:**

```
Size of each element of list in bytes:  48
Size of the whole list in bytes:  48000
Size of each element of the Numpy array in bytes:  8
Size of the whole Numpy array in bytes:  8000
```

**Example 2: Time comparison between Numpy array and Python lists**
In this example, 2 Python lists and 2 Numpy arrays will be created and each container has 1000000 elements. Multiplication of elements in both the lists and Numpy arrays respectively will be carried out and the difference in time needed for the execution for both the containers will be analyzed to determine which one takes less time to perform the operation.

Below is the implementation.

*filter_none*

*edit*

*play_arrow*

*brightness_4*

```
# importing required packages ``import` `numpy ``import` `time `` ` `# size of arrays and lists ``size ``=` `1000000` ` ` `# declaring lists ``list1 ``=` `range``(size) ``list2 ``=` `range``(size) `` ` `# declaring arrays ``array1 ``=` `numpy.arange(size)  ``array2 ``=` `numpy.arange(size) `` ` `# capturing time before the multiplication of Python lists ``initialTime ``=` `time.time() `` ` `# multiplying elements of both the lists and stored in another list ``resultantList ``=` `[(a ``*` `b) ``for` `a, b ``in` `zip``(list1, list2)] `` ` `# calculating execution time ``print``(``"Time taken by Lists to perform multiplication:"``, ``   ``(time.time() ``-` `initialTime), ``   ``"seconds"``) `` ` `# capturing time before the multiplication of Numpy arrays ``initialTime ``=` `time.time() `` ` `# multiplying elements of both the Numpy arrays and stored in another Numpy array ``resultantArray ``=` `array1 ``*` `array2 `` ` `# calculating execution time ``print``(``"Time taken by NumPy Arrays to perform multiplication:"``, ``   ``(time.time() ``-` `initialTime), ``   ``"seconds"``) 
```

**Output:**

```
Time taken by Lists : 0.15030384063720703 seconds
Time taken by NumPy Arrays : 0.005921125411987305 seconds
```

**Example 3: Effect of operations on Numpy array and Python Lists**
In this example, the incapability of the Python list to carry out a basic operation is demonstrated. A Python list and a Numpy array having the same elements will be declared and an integer will be added to increment each element of the container by that integer value without looping statements. The effect of this operation on the Numpy array and Python list will be analyzed.

Below is the implementation.

*filter_none*

*edit*

*play_arrow*

*brightness_4*

```
# importing Numpy package ``import` `numpy as np `` ` `# declaring a list ``ls ``=``[``1``, ``2``, ``3``] `` ` `# converting the list into a Numpy array ``arr ``=` `np.array(ls) `` ` `try``: ``  ``# adding 4 to each element of list ``  ``ls ``=` `ls ``+` `4``   ` `except``(TypeError): ``  ``print``(``"Lists don't support list + int"``) `` ` `# now on array ``try``: ``  ``# adding 4 to each element of Numpy array ``  ``arr ``=` `arr ``+` `4`` ` `  ``# printing the Numpy array ``  ``print``(``"Modified Numpy array: "``,arr) ``   ` `except``(TypeError): ``  ``print``(``"Numpy arrays don't support list + int"``) 
```

**Output:**

```
Lists don't support list + int
Modified Numpy array: [5 6 7]
```