# Numpy Introduction
# -) Numpy is python library designed for scientific computation.
# -) Numpy Arrys are the main way to use Numpy Library.
# -) It is really fast as compared to python list.
# -) It is fast beacause it has binding with c programming language.

# -) 1-d array = vector
# -) 2-d array = matrix
# -) n-d array = tensor

# its a convention to use 'np' as alias, we can change it if we want.
import numpy as np

# Creating ndarrays
# The easiest way to create an array is to use the array function. This accepts any sequence-like object (including
# other arrays) and produces a new NumPy array con‐taining the passed data. For example, a list is a good 
# candidate for conversion.
data = [6, 7.5, 8, 0, 1]
arr = np.array(data) # this is 1-d array or vector
print(arr)  

# Nested sequences, like a list of equal-length lists, will be converted into a multidimensional array:

data1 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data1)
print(arr1)