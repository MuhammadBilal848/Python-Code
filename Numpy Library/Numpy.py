#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# # Numpy - Array Creation and some Attributes

# In[94]:


# Creating ndarrays
# The easiest way to create an array is to use the array function. This accepts any sequence-like object (including
# other arrays) and produces a new NumPy array con‐taining the passed data. For example, a list is a good 
# candidate for conversion.
print('                                making of 1-d array',end='\n\n')
data = [6, 7.5, 8, 0, 1]
arr = np.array(data) # this is 1-d array or vector
print(arr)


# Nested sequences, like a list of "equal-length lists", will be converted into a multidimensional array:
print('                                making of nd-array',end='\n\n')
data1 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data1) # this is 2-d array or matrix
print(arr1)


# Now the above array is 2d array and to confirm this we can use 'ndim' attribute.
# ndim represents the number of dimensions (axes) of the ndarray.
# we can also identify dimension by counting number of brackets on the closing and opening ends of an arry.
print('                                identifying dimensions of an array',end='\n\n')
print(arr.ndim)
print(arr1.ndim)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Now how can we indentify the shape of an array to confrin this we can use 'shape' attribute.
# shape is a tuple of integers representing the size of the ndarray in each dimension.
print('                                identifying shape of an array',end='\n\n')
print(arr.shape)
print(arr1.shape)


# To check data type of an array we can use 'dtype' attribute.
print('                                identifying data type of an array',end='\n\n')
print(arr.dtype)
print(arr1.dtype)


# In addition to np.array, there are a number of other functions for creating new
# arrays. As examples, zeros and ones create arrays of 0s or 1s, respectively, with a
# given length or shape.
# np.empty creates an array without initializing its values to any par‐
# ticular value. To create a higher dimensional array with these methods, pass a tuple
# for the shape.
print('                                making of zero valued array',end='\n\n')
z = np.zeros((5,5))
print(z)
z1 = np.zeros(4)
print(z1)
# another function to make array is zeros_line(Return an array of zeros with the same shape and type as a given array)
p = np.array([[1,2,3,4] , [5,6,7,8]])# this is the array that i have created with different integers and now gonna pass this
# in zeros_like which convert all the different integers into 0s
print(np.zeros_like(p))
# __________ OR ______________
print(np.zeros_like([[1,2,3,4],[1,2,3,4]]))
# we cannot pass this as shape(like this (2,3) , it will consider 2,3 as two values in an array and replace these values with 0's
print(np.zeros_like((2,3)))


print('                                making of one valued array',end='\n\n')
o = np.ones((5,5))
print(o)
print(np.ones(4))
# another function to make array is ones_line(Return an array of ones with the same shape and type as a given array)
a = np.array([[1,2,3,4] , [5,6,7,8]]) # this is the array that i have created with different integers and now gonna pass this
# in ones_like which convert all the different integers into 1s
print(np.ones_like(a))
# __________ OR ______________
print(np.ones_like([[1,2,3,4],[1,2,3,4]]))
# we cannot pass this as shape(like this (2,3) , it will consider 2,3 as two values in an array and replace these values with 1's
print(np.ones_like((2,3)))

print('                                making of empty valued array',end='\n\n')
# empty will return a new array of given shape and type, without initializing entries(he items in the array have not had their
# values set and are just taking the value that was held in memory until you explicitly assign them a value. Sometimes this value
# is 0 or close to it, but there is no guarantee what was in memory at those locations. )
# It’s not safe to assume that np.empty will return an array of all zeros. In some cases, it may return uninitialized “garbage” value
e = np.empty(9) # we can also pass like this (2,2) ,[2,4] or just 5
print(e)
print(np.empty((4,4)))
# another function to make array is ones_like(Return an array of ones with the same shape and type as a given array)
a = np.array([[1., 2., 3.],[4.,5.,6.]])
print(np.empty_like(a))
print(np.empty_like([[1,2,3], [4,5,6]]))
# we cannot pass this as shape(like this (2,3) , it will consider 2,3 as two values in an array and replace these values with garbage values.
print(np.empty_like((2,3)))

print('                                 making of full valued array',end='\n\n')
print(np.full(3,10)) # here 2nd parameter which is fill_value has not any default value if we dont give this any argument
# then it will cause error and the value that we pass in fill_value will be shown in the array.
print(np.full((3,4),'Numpy'))
print(np.full((3,4),5.5))
# another function to make array is full_like(Return an array of ones with the same shape and type as a given array)
a = np.array([[1., 2., 3.],[4.,5.,6.]]) 
print(np.full_like(a,0.9999))
print(np.full_like([[1., 2., 3.],[4.,5.,6.]],125))
# we cannot pass this as shape(like this (2,3) , it will consider 2,3 as two values in an array and replace these values with filled value.
print(np.full_like((2,2),9))

print('                              making of identity matrix',end = '\n\n')
# to create identity(1s on the diagonal and 0s elsewhere) matrix we can use eye function or identity function
# eye function's first parameter is no. of rows and second parameter is coloumn, if we forget to pass no. of coloumn its by default set to no. of rows
print(np.eye(4))
print(np.eye(4,5))
# identity function's first parameter is 'n' which works for both rows as well as coloumn. 
print(np.identity(5))


print('                              making an array using numpy''s range function',end='\n\n')
# if we want to generate a sequence of numbers we can use 'arange function'(arange is an array-valued version of the built-in Python range function)
# Returns
# arange : ndarray
#     Array of evenly spaced values.
arr = np.arange(0,50,2)
print(arr)
arr1 = np.arange(100)
print(arr1)


# # Numpy - Data Types for ndarrays

# In[95]:


# print('                              data type conversion')
# we can change the data type of an array to int, float or any other dtype(data types)
# The numerical dtypes are named the same way: a type name, like float or int, followed by a number 
# indicating the number of bits per element.
print(np.array([1,2,3,4],dtype = np.float64))
arr1 = np.array([1, 2, 3], dtype = np.int32)
print(arr1)
print(arr1.dtype)
# there are many data type such as float16,float32,float64,int9,int16,int32,int64

# we can explicitly convert or cast an array from one dtype to another using ndarray’s astype method.
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
# astype's first parameter is dtype , in which we pass that dtype which we want previous one to replace with.
f_arr = arr.astype(np.float16)
print(f_arr, f_arr.dtype)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
i_arr = arr.astype(np.int8)
print(i_arr, i_arr.dtype)
# In this example, integers were cast to floating point. If I cast some floating-point
# numbers to be of integer dtype, the decimal part will be truncated.


# If you have an array of strings representing numbers, you can use astype to convert
# them to numeric form.
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
non_n_s = numeric_strings.astype(np.float64)
print(non_n_s)
# It’s important to be cautious when using the numpy.string_ type, as string data in NumPy is fixed size and may truncate 
# input without warning. 
# If casting were to fail for some reason (like a string that cannot be converted to
# float64), a ValueError will be raised.(e.g. if an array have values that are text completely)

a = np.arange(0,50,2)
ary = a.astype(str)
print(ary)

# we can also use dtype attribute to change the data type of an array
int_arr = np.arange(0,100,6)
f_arr = np.array([1.2,2.2,3.4,5.6,7.7,-9.0],dtype = np.float64) 
print(int_arr,int_arr.dtype)
conv = int_arr.astype(f_arr.dtype)
print(conv,conv.dtype)
# NOTE: Important thing to remember about astype is that Calling "astype always creates a new array (a copy of the data), even
# if the new dtype is the same as the old dtype."



# There are shorthand type code strings you can also use to refer to a dtype.
print(np.array([1,2,3,4],dtype = 'u8' )) # u8 is a type code for int65/uint64 we can also yse i8 as well instead of u8.
# there are many data type and type codes available(visit Python for Aata Analysis by Wes McKinney book pg. no 91)


# In[ ]:




