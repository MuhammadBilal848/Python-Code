#!/usr/bin/env python
# coding: utf-8

# # Numpy Introduction
# * Numpy is python package designed for scientific computation.
# * Numpy Arrys are the main reason to use Numpy Library.
# * It is really fast as compared to python list.
# * It is fast beacause it has binding with c programming language.

# In[14]:


import numpy as np


# # Numpy - Array Creation and some Attributes
# * 1-d array = vector
# * 2-d array = matrix
# * n-d array = tensor

# In[70]:


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


# To check how many elements does an array has we can use 'size' attribute.
print('                                identifying how many elements are there in an array',end='\n\n')
print(arr.size)
print(arr1.size)

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
# $$$$ It’s not safe to assume that np.empty will return an array of all zeros. In some cases, it may return uninitialized “garbage” value
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
print(np.eye(4,5))# this is not a square matrix so the diagonal still will contain ones but due to an extra column it will skip that column
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

print('                             making an array using numpy''s linspace',end = "\n\n")
# if we want to create an array of evenly spaced numbers we can use linspace function
arr = np.linspace(0,5,10) # first argument is start second is stop and this is how many points/values we want between 0 to 5 
# in our array. so this array will return 10 points/values between 0 to 5.
print(arr)




print('                             shaping of an array')
print(np.zeros(2)) # this means make an array which have two element(len of number shows dimensions here dim is 1)
print(np.zeros((2,3))) # this means make an array which have two rows and 3 columns(len of number shows dimensions here dim is 2)
print(np.zeros((2,3,5,4))) # this means make 6(2,3 = 2*3) arrays of 5 rows and 4 column, rows and column numbers alawys in the end
print(np.zeros((2,3,4,2,1))) # this means make 24(2,3,4 = 2*3*4) arrays of 2 rows and 1 column 
# shape - (no of elements)
# shape - (no or rows, no of column)
# shape - (no of arrays , no of arrays , ..., no. of rows, no. of column)


# # Numpy - Data Types for ndarrays

# In[69]:


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
print(np.array([1,2,3,4],dtype = 'u8' )) # u8 is a type code for int65/uint64 we can also sse i8 as well instead of u8.
# there are many data type and type codes available(visit Python for Aata Analysis by Wes McKinney book pg. no 91)

'''
##########################################################################################################################
'''

# Another thing to remember is that, if we change the data type of any single element in an array which (array) prior has
# same data type for all the elements, the change in dtype of single element of an array would result in changing dtype of
# all the elements to this single element dtype.
arr = np.array([1,2,3,4,5,6])
print(arr,arr.dtype) # in this array the data type of all the elements is int.
# to float
arr = np.array([1,2,3,4,5,6.0]) # here is changed the last element 6 to 6.0 which converts all the other elements dtype to float
print(arr,arr.dtype)
# to string
arr = np.array([1,2,3,4,5,'6']) # here is changed the last element 6 to 6.0 which converts all the other elements dtype to float
print(arr,arr.dtype) 


# # Numpy - Arithmetic with NumPy Arrays

# In[101]:


# Any arithmetic operations between equal-size arrays applies the operation element-wise.
# Arthimetic operations in numpy applies on each and every element of an array.
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr * arr)
print(arr - arr)

# Arithmetic operations with scalars(only magnitude,a number, size) propagate the scalar argument to each element in the
# array.
print(1/arr)
print(arr ** 0.5)


# Comparisons between arrays of the same size yield boolean arrays.
arr2 = np.array([[0, 4, 1], [7, 2, 12]])
print(arr2)
print(arr2 > arr)
print(arr2==arr)
print(arr < arr2)
print(arr2 != arr)
# Operations between differently sized arrays is called broadcasting and will be discussed later.


# # Numpy - Basic Indexing and Slicing

# In[99]:


# NumPy array indexing is a rich topic, as there are many ways you may want to select
# a subset of your data or individual elements. 
# One-dimensional arrays are simple on the surface they act similarly to Python lists.
arr = np.arange(11)
print(arr)
print(arr[6])
print(arr[4:8])
arr[5:8] = 0
print(arr)
# As you can see, if you assign a scalar value to a slice, as in arr[5:8] = 0, the value is
# propagated (or broadcasted henceforth) to the entire selection. An important first dis‐
# tinction from Python’s built-in lists is that array slices are views on the original array.
# This means that the data is not copied, and any modifications to the view will be
# reflected in the source array.
# To give an example of this, I first create a slice of arr.
arr_slice = arr[5:8]
print(arr_slice)
# Now, when I change values in arr_slice, the mutations are reflected in the original array arr.
arr_slice[1] = -9 # this change will push in my original array in which i have assigned zeros
print(arr)
# The “bare” slice [:] will assign to all values in an array.
arr_slice[:] = 64
print(arr)
# If you are new to NumPy, you might be surprised by this, especially if you have used
# other array programming languages that copy data more eagerly. As NumPy has been
# designed to be able to work with very large arrays, you could imagine performance
# and memory problems if NumPy insisted on always copying data.

# What are views of an array?
# As its name is saying, it is simply another way of viewing the data of the array.
# Technically, that means that the data of both objects is shared. You can create views by selecting a slice of
# the original array, or also by changing the dtype (or a combination of both). These different kinds of views 
# are described below.
# more on this,
# [https://scipy-cookbook.readthedocs.io/items/ViewsVsCopies.html#:~:text=What%20is%20a%20view%20of,of%20both%20objects%20is%20shared.]


# $$$ If you want a copy of a slice of an ndarray instead of a view, you
# will need to explicitly copy the array—for example, arr[5:8].copy()[by value copy].
b = arr[5:8].copy()
print(b)


# With higher dimensional arrays, you have many more options. In a two-dimensional
# array, the elements at each index are no longer scalars but rather one-dimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d[2][1])
# Thus, individual elements can be accessed recursively. But that is a bit too much
# work, so you can pass a comma-separated list of indices to select individual elements.
# So these are equivalent,
print(arr2d[2,1])

# See Figure 4-1 for an illustration of indexing on a two-dimensional array. I find it
# helpful to think of axis 0 as the “rows” of the array and axis 1 as the “columns.” 
# 1) AXIS 0 IS THE DIRECTION ALONG THE ROWS , axis 0 is the axis that runs downward down the rows(which means that any change 
# in axis 0 will apply to column)
# 2) AXIS 1 IS THE DIRECTION ALONG THE COLUMN , axis 1 is the axis that runs horizontally across the columns(which means that
# any change in axis 1 will apply to rows) 
'''
Reliable source to understand the axises of an array is , 
[https://www.sharpsightlabs.com/blog/numpy-axes-explained/]
(visit Python for Data Analysis by Wes McKinney book pg. no 96) for figure 4-1
another site to understand axises is , [https://discuss.codecademy.com/t/what-is-an-axis-in-numpy/359666] 
but the link above is highly recomended.
'''

# In multidimensional arrays, if you omit later indices, the returned object will be a
# lower dimensional ndarray consisting of all the data along the higher dimensions. So
# in the 2 × 2 × 3 array arr3d.
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3d)
# arr3d[0] is a 2 × 3 array:
print(arr3d)

# Both scalar values and arrays can be assigned to arr3d[0]:
old_values = arr3d[0].copy()

arr3d[0] = 2020
print(arr3d)

arr3d[0] = old_values
print(arr3d)

# Similarly, arr3d[1, 0] gives you all of the values whose indices start with (1, 0),
# forming a 1-dimensional array.
print(arr3d[1,0])

# The below expression is the same as though we had indexed in two steps.
x = arr3d[1]
print(x[0])
# Note that in all of these cases where subsections of the array have been selected, the
# returned arrays are views.


# # Numpy - Indexing with slices

# In[173]:


# Like one-dimensional objects such as Python lists, ndarrays can be sliced with the
# familiar syntax
arr = np.arange(0,50,4)
print(arr[1:5])

# Consider the two-dimensional array arr2d, Slicing this array is a bit different.
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[:2])
# As you can see, it has sliced along axis 0, the first axis. A slice, therefore, selects a
# range of elements along an axis. It can be helpful to read the expression arr2d[:2] as
# “select the first two rows of arr2d"

# You can pass multiple slices just like you can pass multiple indexes.
print(arr2d[:2, 1:]) # the first slice(:2) will give us the access of start two rows of an arrays, and second slice(1:) will 
# help us slice/edit the column of selected rows
# generally - [row,column]

print(arr2d[1,:2]) # the first slice(:2) will give us the access of 1-indexed arrays, and second slice(:2) will help us slice/edit  
# selected ararys.

# Similarly, I can select the third column but only the first two rows like so.
print(arr2d[:2,2])

# Note that a colon by itself means to take the entire axis, so you can slice only higher dimensional axes by doing
print(arr2d[:,1])

# Of course, assigning to a slice expression assigns to the whole selection:
arr2d[:2, 1:] = 2020
print(arr2d)


a = np.ones((8,8))
a[1:-1,1:-1] = 0
print(a)


# # Indexing Practice

# In[54]:


a = np.zeros((20,20))
print(a)
var = 1
for i in range(len(a)): # 20
    a[i,i] = 1
    a[i,-var] = 1
    var += 1
print(a)

# making alternate columns 1
for i in range(len(a)): # 20
    a[i,1::2] = 1
print(a)

# making alternate element 1 of 1st row , 1st column and last row , last column
a[0,::2] = 1
a[:,0][::2] = 1
a[-1,::2] = 1
a[:,-1][::2] = 1
print(a)
# __________________ OR __________________
a[[0,-1],::2] = 1
a[::2,[0,-1]] = 1
print(a)

for i in range(len(a)): # 0,1,2,3,4,5,6,7,8,9,....20
    if (i%2!=0) and (i<=10): # 1,3 is odd == True
        a[i,i:-i] = 1 # a[1,1:-1],a[3,3:-3] , a[11,11]
        a[i:-i,i] = 1
        a[-i-1,i:-i] = 1
        a[i:-i,-i-1] = 1

print(a)


# # Numpy - Boolean Indexing

# In[105]:


# Let’s consider an example where we have some data in an array and an array of names
# with duplicates. I’m going to use here the randn function in numpy.random to generate
# some random normally distributed data:
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
# print(names)
data = np.random.randn(7,4)
print(data)
# Suppose each name corresponds to a row in the data array and we wanted to select
# all the rows with corresponding name 'Bob'. Like arithmetic operations, compari‐
# sons (such as ==) with arrays are also vectorized. Thus, comparing names with the
# string 'Bob' yields a boolean array.
print(names == 'Bob') # since arthimetic operations in numpy applies on each and every element of an array and in this array
# this will return boolan arrays.
print(data[names == 'Bob']) # in this step what we've done is we have pasted/overlaped our boolean array(as index value) which we
# have created above, due to which whichever index that has 'True' value will be replaced by the same index number in data array
# and rest of the index values wihch have 'False' will also be removed from data array.  
# so in boolean array only 0 and 3 has 'True' value so in data array only 0 and 3 
# index number will be left and others will be removed.
# passing boolean array as index is a method to paste/overlap data.

# The boolean array must be of the same length as the array axis it’s indexing. You can
# even mix and match boolean arrays with slices or integers

# $$$ Boolean selection will not fail if the boolean array is not the correct
# length, so I recommend care when using this feature.


# I select from the rows where names == 'Bob' and index the columns, too. [means that code before comma is for rows and code 
# after comma is for column] --or-- [rows,column]
print(data[names == 'Bob',1])
# print(data[(names == 'Bob'),2])
# print(data[(names == 'Bob'),1:])

# To select everything but 'Bob', you can either use != or negate the condition using ~:
print(names != 'Bob')
print(data[names != 'Bob'])

# -------------- OR --------------

cond = names == 'Bob'
print(data[~(cond)])
# The ~(tilde) operator can be useful when you want to invert a general condition:

# Selecting two of the three names to combine multiple boolean conditions, use
# boolean arithmetic operators like & (and) and | (or):
new = (names == 'Bob') | (names == 'Will')
print(new)
print(data[new])
# Selecting data from an array by boolean indexing always creates a copy of the data,
# even if the returned array is unchanged.
# $$$ The Python keywords and and or do not work with boolean arrays. Use & (and) and | (or) instead.

print(data[data>0]) # here data>0 will create a boolean array in which all the index filled with True which holds value greater
# than 0 and rest of them filled with False, and as we passed this bool array as index on our data var so this will bring all the
# values greater than 0

# Setting values with boolean arrays works in a common-sense way. To set all of the
# negative values in data to 0 we need only do
data[data < 0 ] = 0
print(data)

# Setting whole rows or columns using a one-dimensional boolean array is also easy:
print(names != 'Joe')
data[names != 'Joe'] = 7
print(data)

# now we will select all the values of names array
sall = names == 'Bill'
data[~(sall)] = 90
print(data)


# # Numpy - Fancy Indexing

# In[129]:


# # Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays.
# suppose we had vector with 6 elements,
arr = np.array([10,11,12,13,14,15,16])
# index #        0  1  2  3  4  5  6
# here, we wanted to select elemnts that are on even index number, one way to do this is,
print(arr[0],arr[2],arr[4],arr[6])
# but with the help of fancy indexing we can do this ,
print(arr[[0,2,4,6]]) # and this will return an array of these numbers.

# Suppose we had an 8 × 4 array.
# Fancy indexing allow us to access those particular rows and column which we want. we just have to pass an array of 
# values(rows,column) 
# consider arr a matrix of 8 x 4 in which we want to select row no 0,2,4 and 6 so we have to pass a list of these numbers in 
# # index as list of list. or To select out a subset of the rows in a particular order, you can simply pass a list or
# ndarray of integers specifying the desired order
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
print(arr[[0,2,4,6]])
# # we can use negetive indexing as well.
print(arr[[-8,-6,-4,-2]])

# # Passing multiple index arrays does something slightly different; it selects a onedimensional array of elements corresponding 
# # to each tuple of indices
arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2]]) # we can still slice columns in this line like this arr[[1, 5, 7, 2],1:2] but cannot select 
# particular column by this way.
print(arr[[1, 5, 7, 2],:]) # here i have passed an array of selected rows and after comma i select all the column(bare slice)
# column 

print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
#   arr[[ selected rows]], [rows content on each index]
# Here the elements (1, 0), (5, 3), (7, 1), and (2, 2) were selected. Regardless of
# how many dimensions the array has (here, only 2), the result of fancy indexing is
# always one-dimensional.

# to select particular column thats what we can do,
print(arr[[1, 5, 7, 2]][:,[0, 3, 1, 2]]) # here i have passed an array of selected rows as list of list as an array index and 
# after that in an other square braces i select all the selected rows through bare slice and after that i have passed an
# array of selected column.
#    [ selected rows ] [ bare slice of row,selected column ]

# another way to select particular column is(but we cannot select particular rows in it),
print(arr[:,[0,1,2]]) # here i select all the rows(bare slice) and after comma i have passed an array of selected column 
#  arr[ bare row slice , selected column]

# A thing to remember is that an array index always have two things one is selection of rows and other is selection of column,
# but if you are doing fancy indexing of an array and have already passed an array of selected rows then you cannot pass another 
# comma seperated array of selected column(because this will bring the contents of selected rows) but can slice column of all
# selected rows comma separated.
print(arr[[0,2,4,6],:][:,[0,1]])
print(arr[[0,2,4,6],:][:,[0,1]][1:3,1:])
#  [row, bare column][bare row,column][sliced row,sliced column]

# Keep in mind that fancy indexing, unlike slicing, always copies the data into a new array


# # Numpy - Transposing Arrays and Swapping Axes

# In[744]:


# Transposing is a special form of reshaping that similarly returns a view on the under‐
# lying data without copying anything. Arrays have the transpose method and also the
# special T attribute
arr = np.arange(24).reshape(6,4)
print(arr.T) # here T used as data discriptor for Transpose we can also use transpose() function
print(arr.transpose())

# we can find dot product of two sets using dot function
# 0-D 
a = 2
b = 3
print(np.dot(a,b))

# 1-D
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(np.dot(a,b)) # a.dot(b) is equivalent to np.dot(a, b):

# 2-D
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
# print(a)
# print(b)
print(a.dot(b))

# # we can also change the axes values in transposition of an array
a = np.array([[1, 2], [3, 4]]) # [1,2] has 0 index number while [3,4] has 1 index number
print(a)
print(a.transpose())
print(a.transpose((1, 0))) # here i changed the array indexes thats why their transpose is different 
print(a.transpose(0,1))

# For higher dimensional arrays, transpose will accept a tuple of axis numbers to permute the axes (for extra mind bending)
# Here "permute" means "rearrange", so rearranging the order of axes.
arr = np.arange(16).reshape((2, 2, 4)) # transpose will return (column,rows,how many of these arrays,,,,,) or 
# this will return (2,2,4)[::-1] = (4,2,2)
print(arr)
print(arr.transpose()) # this will return the transpose of reverse reshape value (4,2,2) 4 arrays of 2 rows and 2 column

# how can we contemplate which index number of transposed array holds which value of previous array? 

# Answer: The shape of arr is (2, 2, 4), for the value 7, you can get the value by arr[0, 1, 3] , after tranpose we just need to
# reverse the value index list and we got our new index number for that value. Here value for 7 arr[0,1,3][::-1] = arr[3,1,0]
#        Real array                     Transposed Array                       
# for zero, arr[0,0,0][::-1] = arr[0,0,0] for tramsposed array
# for one , arr[0,0,1][::-1] = arr[1,0,0] for tramsposed array
# for two , arr[0,0,2][::-1] = arr[2,0,0] for tramsposed array
# for three , arr[0,0,3][::-1] = arr[3,0,0] and so onnnnnnn..


# if we want to change the transpose axes we can pass the index of reshape values as axes in transpose as tuple
print(arr.transpose((1,0,2))) # (2,2,4) since we've changed the shape of transpose.
# Here, the axes have been reordered with the second axis first, the first axis second, and the last axis unchanged.

# here we are considering the reverse of only two axes(1st,2nd)(because we just reordered 0 and 1 axis) and third remains the same.
# we always consider the reverse of those index number which have been reordered
#        Real array                 Transposed Array                       
# for zero, arr[0,0,0][::-1] = [0,0] to be clear [0,0,0]
# for one , arr[0,0,1][::-1] = [0,0] to be clear [0,0,1]
# for two , arr[0,0,2][::-1] = [0,0] to be clear [0,0,2]
# for three , arr[0,0,3][::-1] = [0,0] to be clear [0,0,3]

# for four , arr[0,1,0][::-1] = [1,0] to be clear [1,0,0]
# for five , arr[0,1,1][::-1] = [1,0] to be clear [1,0,1]
# for six , arr[0,1,2][::-1] = [1,0] to be clear [1,0,2]
# for seven , arr[0,1,3][::-1] = [1,0] to be clear [1,0,3]
# and so onnnn... 
# thats how an array change its axises

# Ndarray has the method swapaxes, which takes a pair of axis numbers and switches the indicated axes to rearrange the data.
arr = np.arange(16).reshape((2, 2, 4)) # here 2(axis) = 0(index number) , 2(axis) = 1(index number) , 4(axis) = 2(index number)
print(arr)
print(arr.swapaxes(1, 2))# what swapaxes does is it will swap the given axes and rearrange the values and reorder the array.
print(arr.swapaxes(1, 2).shape)
# here we have swapped axis 1 and axis 2 which means we have swapped the value of axis 1 by axis 2 and axis 2 by axis 1
# previous array index number (0,1,2)   ,     current array index number (0,2,1)
# previous array value number (2,2,4)   ,     current array value number (2,4,2)
# the same way use to determine the index values for swap array which we use for transpose.
 
# another way to determine the value change is,
print(arr.swapaxes(1, 2).ravel()) # ravel is a function which return a contiguous flattened array. 

'''
for more details about swapaxes works [https://stackoverflow.com/questions/42312670/how-does-numpy-swapaxes-work?rq=1]
for more details about tranpose works [https://stackoverflow.com/questions/32034237/how-does-numpys-transpose-method-permute-the-axes-of-an-array]
YT video on transpose array [https://www.youtube.com/watch?v=5vT553CSxas]
'''


# # Numpy - Universal Functions: Fast Element-Wise Array Functions

# In[93]:


# A universal function, or ufunc, is a function that performs element-wise operations
# on data in ndarrays. You can think of them as fast vectorized wrappers for simple
# functions that take one or more scalar values and produce one or more scalar results.

# Many ufuncs are simple element-wise transformations, like sqrt or exp:
arr = np.arange(10)
print(arr,end='\n\n')

# Functions which takes single array as argument are called 'unary ufuncs' [unary means single component or element]

print('             Square Root')
# for square root
print(np.sqrt(arr),end='\n\n') # square root of all numbers from 0 to 10

print('             Exponent')
# for exponent 
print(np.exp(arr),end='\n\n') # this will calculate exponential of all elements (e**0 , e**1 , e**2 , e**3 ,....)

# Functions which takes two array as argument are called 'binary ufuncs' [binary means double component or element]

print('             Maximum')
# to find maximum of between two arrays, numpy has function called 'maximum'
x = np.random.randn(10)
y = np.random.randn(10)
print(np.maximum(x,y),end='\n\n')
# Here, numpy.maximum computed the element-wise maximum of the elements in x and y.

# While not common, a ufunc can return multiple arrays. modf is one example, a vec‐
# torized version of the built-in Python divmod(a python function which takes two numbers
# and returns a pair of numbers consisting of their quotient and remainder.) it returns the fractional and integral
# parts of a floating-point array.

arr = np.random.randn(7)*5
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)


# Ufuncs accept an optional out argument that allows them to operate in-place on array.
print(np.sqrt(arr)) # since square root of -ve numbers is not posibble, so numpy shows "nan(no a number)" on those value. this
# will not affect my original array or will not save this array in place of my original array.
# print(arr) # here we can see there is no change in my original array

# if we wamt to make the change global or to want to keep the array value same as changed array value for this we can use
# another arugment of sqrt function which is 'out'(its basically a location/var where you want to to save changed array but it 
# must have shape same as the array we want to store)
a = np.zeros(7) # this is of same shape as square root array.
print(np.sqrt(arr,a)) # here i have saved my square root array in variable a which now is my square root array.
print(a)
print(arr) # still orignal array is not affected
# we can also save the value in same array on which we have applied square root.
print(np.sqrt(arr,arr))
print(arr) # now this will affect and change my original array to sqaure root arary.

# some more unary ufuncs

print('                           square() ',end='\n\n')
# to square all the numbers in an array we can use square function.
arr = np.arange(10)
print(np.square(arr))

print('                            abs()', end = '\n\n')
# abs() or absolute() or fabs() function will return the distance of each element of an array from zero.
arr = np.array([1, -3, 15, -466]) # this works like that, 1 is at 1 distance from zero, -3 is at 3 distance from zero and so on..
print(arr)
print(np.abs(arr))

print('                           sign()',end='\n\n')
# to know which number in an array is +ve and which one is -ve and which one is zero
# a functon named 'sign' will take an array as argument and return an array of 0(for zero),1(for +ve),-1(for -ve)
a = np.random.randn(10)
print(a)
print(np.sign(a))

print('                            ceil()',end='\n\n')
# ciel function will return the next higher integer of each element of  an array.
arr = np.array([0.1,2.3,4.5,-9.6,5.2,3.3,-1.0,1,2]) # this works like that, higher integer after 0.1 is 1 and higher
# integer after -9.6 is -9 and so on....
print(arr)
print(np.ceil(arr))

print('                            floor',end='\n\n')
# floor function is the opposite of ceil function and returns next lower integer of each element of an array.
arr = np.array([0.1,2.3,4.8,-9.6,5.2,3.3,-1.0,1,2])
print(arr)
print(np.floor(arr))

print('                            rint()',end='\n\n')
# rint function Round elements to the nearest integer, preserving the dtype.
a = np.random.randn(10)
print(a)
print(np.rint(a))
print(arr)
print(np.rint(arr)) 

print('                           isnan()',end='\n\n')
arr = np.random.randn(10)
np.sqrt(arr,arr)
print(arr)
print(np.isnan(arr))

print('                           trigonometry functions')
a = np.array([0,30,45,60,90])
print(np.cos(a)) # return value will be radian converted
print(np.sin(a)) # return value will be radian convert
print(np.tan(a))
# for more unary ufuncs (visit Python for Aata Analysis by Wes McKinney book pg. no 107) for figure 4-3

# some more Binary ufuncs

x = np.random.randn(8)
print(x)
y = np.random.randn(8)
print(y)

print('                            add()',end = '\n\n')
# Add corresponding elements in arrays
print(np.add(x,y)) 

print('                            subtract()',end = '\n\n')
# Subtract elements in second array from first array
print(np.subtract(x,y))

print('                            multiply()',end = '\n\n')
# Multiply array elements
print(np.multiply(x,y))

print('                            divide() , floor_divide',end = '\n\n')
#Divide or floor divide (truncating the remainder)
print(np.divide(x,y)) # this will nor truncate the reaminder 
print(np.floor_divide(x,y)) # this will truncate the remainder

print('                            minimum() , fmin()',end = '\n\n')
# Element-wise minimum; fmin ignores NaN
print(np.minimum(x,np.sqrt(y))) # this will not ignore the nan and bring nan instead of value thas in the comparison
print(np.fmin(x,np.sqrt(y))) # this will ignore nan and bring the value thats in the comparison

print('                            maximum() , fmin()',end = '\n\n')
# Element-wise maximum; fmin ignores NaN
print(np.maximum(x,np.sqrt(y))) # this will not ignore the nan and bring nan instead of value thas in the comparison
print(np.fmax(x,np.sqrt(y))) # this will ignore nan and bring the value thats in the comparison

print('                            mod() ',end = '\n\n')
# Element-wise modulus (remainder of division)
print(np.mod(x,y)) 
 
print('                         copysign()',end = '\n\n')
# copysign Copy sign of values in second argument to values in first argument
print(np.copysign(x,y)) # here this will change the sign of y to x or the signs which belongs to y now belongs to x

# for more binary ufuncs (visit Python for Aata Analysis by Wes McKinney book pg. no 107) for figure 4-4


# # Numpy - Array Oriented Programming with Arrays

# In[30]:


points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
print(ys)
print(xs)
# grid(a network of lines that cross each other to form a series of squares or rectangles.)
# meshgrid function helps in creating array of coordinate values because to create a grid we need each and every possible
# coordinate and we can do this easily using meshgrid function. 
# which is used to create a rectangular grid out of two given one-dimensional arrays.
# here xs(returned by meshgrid) is simple 2-D array but yx is the transpose of the xs array due to which every combination of 
# coordinate is possible.
# Thats how a grid looks like [https://i.stack.imgur.com/1xeW8.png]

# some simple examples of meshgrid function,

# to understand the rows and columns of meshgrid function,
# meshgrid(array-length = column,array-length = rows)
#                   column = 5     row = 3
a,b = np.meshgrid(np.arange(0,5),np.arange(6,9))
# so row = 3 and column = 5 so shape would be (3,5)
print(a,a.shape)
print(b,b.shape)

# using meshgrid with same size array
xvalues = np.array([0,1,2,3,4]) # len of this array is 5 (len of this array considered as column)
yvalues = np.array([0,1,2,3,4]) # len of this array is 5 (len of this array considered as row)
# here xvalues and yvalues are of same length
x,y = np.meshgrid(xvalues,yvalues)
# here xvalues has 5(column) values and yvalues has also 5(row) values which means that meshgrid will create 5x5 matrix from 
# the same 'xvalues' array with repeative row(which will later assgin in x) and the transposed array of yvalues with repeative
# column will be assigned to y with the same array shape((xvalues)column=5, (yvalues)row=5 == 5x5 ).
# Thing to remeber here is that the shape of array will never going to change it will be constant, here transpose will always be
# of second argument/array(in this case 'yvalues') and the shape remains constant for the transposed array as well as the first
# array.
print(x)
print(y)


# using meshgrid with different size array
xv = np.array([0,1,2,3,4,5,6,7]) # len of this array is 8 (len of this array considered as column)
yv = np.array([0,1,2,3,4,5]) # len of this array is 6 (len of this array considered as rows)
# here xv and yv are not of same length
x,y = np.meshgrid(xv,yv)
# here xv has 8(column) values and yv has also 6(row) values which means that meshgrid will create 6x8 matrix from 
# the same 'xv' array with repeative row(which will later assgin in x) and the transposed array of yv with repeative
# column will be assigned to y with the same array shape((xv)column=8, (yv)row=6 == 8x6 ).
print(x, x.shape)
print(y, y.shape)
# the mesgrid function will manage the rows and columns itself, 

# SPARSE PARAMETER IN MESHGRID
x,y = np.meshgrid(xv,yv,sparse = True)
# We observe that x is a row repeated matrix whereas y is a column repeated matrix. One row of x and one column of y
# is enough to determine the positions of all the points as the other values will get repeated over and over. So we can edit 
# above code as follows: OR when sparse parameter will be True it will return only first row and first column of first and 
# second array respectively.
print(x)
print(y) 

# two functions orgrid(in this sparse is True and takes ) and mgrid(in this sparse is False ) are pretty same as meshgrid
x , y = np.ogrid[0:4,0:4]
print(x)
print(y)

x,y = np.mgrid[0:8,0:6] # mgrid is basically the transpose of meshgrid. look for 'using meshgrid with different size array'.
print(x)
print(y)

'''
for more detail regarding meshgrid visit [https://www.geeksforgeeks.org/numpy-meshgrid-function/#:~:text=string%20in%20Python-,Numpy%20Meshgrid%20function,Cartesian%20indexing%20or%20Matrix%20indexing.]
and [https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy]
for more detail regarding mgrid visit [http://louistiao.me/posts/numpy-mgrid-vs-meshgrid/#id2]
for more detail regarding mgrid visit [https://towardsdatascience.com/the-little-known-ogrid-function-in-numpy-19ead3bdae40]
'''


# # Numpy - Expressing Conditional Logic as Array Operations

# In[52]:


# The numpy.where function is a vectorized version of the ternary expression x if condition else y. Suppose we had a
# boolean array and two arrays of values:
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# Suppose we wanted to take a value from xarr whenever the corresponding value in cond is True, and otherwise take the value 
# from yarr. A list comprehension doing this might look like:
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
# This has multiple problems. First, it will not be very fast for large arrays (because all the work is being done in
# interpreted Python code). Second, it will not work with multidimensional arrays. With np.where you can write 
# this very concisely:
result = np.where(cond, xarr, yarr)
print(result)


# generally, np.where works like this,
#                 1       2        3
# np.where(condition,option-A,option-B)
# 1)The condition 
# 2)What to do with entities for which the condition is True.
# 3)What to do with entities for which the condition is False.



# The second and third arguments to np.where don’t need to be arrays; one or both of them can be scalars. A typical use of
# where in data analysis is to produce a new array of values based on another array. Suppose you had a matrix of randomly
# generated data and you wanted to replace all positive values with 2 and all negative values with –2. This is very easy 
# to do with np.where:
arr = np.random.randn(4, 4)
print(arr)
print(arr>0)
result1 = np.where(a>0,2,-2)
print(result1)
# You can combine scalars and arrays when using np.where. For example, I can replace all positive values in arr with
# the constant 2 like so:
result2 = np.where(arr > 0, 2, arr) # set only positive values to 2
print(result2)
# The arrays passed to np.where can be more than just equal-sized arrays or scalars.


# # Numpy - Mathematical and Statistical Methods

# In[99]:


# A set of mathematical functions that compute statistics about an entire array or about
# the data along an axis are accessible as methods of the array class. You can use aggre‐
# gations (often called reductions) like sum, mean, and std (standard deviation) either by
# calling the array instance method or using the top-level NumPy function.
# To explain what I mean by “aggregate,” I’ll give you a simple example.
# Imagine you have a set of 5 numbers. If sum up those 5 numbers, the result will be a single number.
# Summation effectively aggregates your data. It collapses a large number of values into a single value.


# Here I generate some normally distributed random data and compute some aggregate
# statistics:
arr = np.random.randn(5, 4)
print(arr)

# to find mean of an entire array we can use mean function,
print(arr.mean())
# OOOOOOOOOOOORRRRRRRRRRRRRRRRRRR
print(np.mean(arr))
 
# to find sum of an entire array we can use sum function,
print(arr.sum())
# OOOOOOOOOOOORRRRRRRRRRRRRRRRRRR
print(np.sum(arr))

# Functions like mean and sum take an optional axis argument that computes the statis‐
# tic over the given axis, resulting in an array with one fewer dimension:
# axis = 0 (will apply across column)
# axis = 1 (will apply across rows)
print(arr.mean(axis=1))
print(arr.sum(axis=0))

# Here, arr.mean(1) means “compute mean across the columns” where arr.sum(0)
# means “compute sum down the rows.”
# Other methods like cumsum and cumprod do not aggregate, instead producing an array
# of the intermediate results:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum()) # thats how comulative sum works [0,0+1,0+1+2,0+1+2+3,0+1+2+3+4,....so onnn]
print(arr.cumprod()) # thats how comulative sum works [0,0*1,0*1*2,0*1*2*3,0*1*2*3*4,....so onnn]


# In multidimensional arrays, accumulation functions like cumsum return an array of
# the same size, but with the partial aggregates computed along the indicated axis
# according to each lower dimensional slice:
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))

# there are also min/minimum and max/maximum function, 
print(arr.min(axis = 1))
print(arr.max(axis = 0))

# another function argmin which returns the index number of minimum value in an array
arr = np.random.randint(1,100,20)
print(arr)
print(min(arr))
print(np.argmin(arr),'index number')

# another function argmax which returns the index number of maximum value in an array
arr = np.random.randint(1,100,20)
print(arr)
print(max(arr))
print(np.argmax(arr),'index number')


# See Table 4-5 for a full listing. (visit Python for Aata Analysis by Wes McKinney book pg. no 112) for Table 4-5


# # Numpy - Methods for Boolean Arrays

# In[255]:


# Boolean values are coerced to 1 (True) and 0 (False) in the preceding methods. Thus,
# sum is often used as a means of counting True values in a boolean array:

arr = np.random.randn(100)
print((arr>0).sum()) # Number of positive values

# There are two additional methods, any and all, useful especially for boolean arrays.
# any tests whether one or more values in an array is True, while all checks if every
# value is True:
bools = np.array([False, False, True, False])
print(bools.any()) # any returns True if any element in an array is True
print(bools.all()) # all returns True if all elements in an array are True

# These methods also work with non-boolean arrays, where non-zero elements evaluate to True.


# # Numpy - Sorting

# In[278]:


# Like Python’s built-in list type, NumPy arrays can be sorted in-place with the sort method:
arr = np.random.randn(6)
print(arr)
arr.sort()
print(arr)

# You can sort each one-dimensional section of values in a multidimensional array inplace along 
# an axis by passing the axis number to sort:
arr1 = np.random.randn(5, 3)
print(arr1)
arr1.sort(1)
print(arr1)
# The top-level method np.sort returns a sorted copy of an array instead of modifying the array in-place.


# # Numpy - Unique and Other Set Logic

# In[109]:


# NumPy has some basic set operations for one-dimensional ndarrays. A commonly
# used one is np.unique, which returns the sorted unique values in an array:
# unique function has four parameters, 
# arr(The input array. Will be flattened if not 1-D array)
# return_index(If True, returns the indices of elements in the input array)
# return_inverse(If True, returns the indices of unique array, which can be used to reconstruct the input array)
# return_counts(If True, returns the number of times the element in unique array appears in the original array)

names = ['Bilal','Abuzar','Usama','Nofil','Zaigham','Hasan','Usama','Abuzar','Zaigham']
names = np.unique(names)
print(names)

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
ints1 = np.unique(ints)
print(ints1)
ints2 = np.unique(ints,return_index=True,return_counts=True)
print(ints2)
# in contrast np.unique with the pure Python alternative: sorted(set(names))


# Another function, numpy.in1d() test whether each element of a 1-D array
# is also present in a second array and return a boolean array the same length as arr1 that is True where 
# an element of arr1 is in arr2 and False otherwise.
# Syntax : numpy.in1d(arr1, arr2, assume_unique = False, invert = False)
# Parameters :
# arr1 : [array_like] Input array.
# arr2 : [array_like] The values against which to test each value of arr1.
# assume_unique : [bool, optional] If True, the input arrays are both assumed to be unique, which can speed up the calculation. Default is False.
# invert : [bool, optional] If True, the values in the returned array are inverted. Default is False.


arr1 = np.array([0, 1, 2, 3, 0, 4, 5,1]) 
arr2 = [0, 2, 5,5] 
result = np.in1d(arr1, arr2) 
result1 = np.in1d(arr1, arr2,invert = True)
result2 = np.in1d(arr1, arr2,invert = True,assume_unique=True)
print(result)
print(result1)
print(result2)

# Another function, Intersect1d Compute the sorted, common elements in x and.
arr1 = np.array([1, 1, 2, 3, 4]) 
arr2 = np.array([2, 1, 4, 6]) 
result = np.intersect1d(arr1, arr2) 
print(result)    

# Another function, union1d(x, y) Compute the sorted union of elements.
arr1 = np.array([1, 1, 2, 3, 4]) 
arr2 = np.array([2, 1, 4, 6]) 
result = np.union1d(arr1, arr2) 
print(result)    

# See Table 4-6 for a listing of set functions in NumPy.
# (visit Python for Aata Analysis by Wes McKinney book pg. no 115) for Table 4-5


# # Numpy - File Input and Output with Arrays

# In[348]:


# NumPy is able to save and load data to and from disk either in text or binary format.
# np.save and np.load are the two workhorse functions for efficiently saving and load‐
# ing array data on disk. Arrays are saved by default in an uncompressed raw binary
# format with file extension .npy:
# np.save('filename.npy',array) if we dont pass file ext(npy) here, numpy will manage itself. 
# np.load('filename.npy')
# np.savez('filename.npz',array1,array2,..)

x = np.array([1,2,3,4,5,6])
y = np.array([7,8,9,10,11])
np.save('test1',x)

# now im going to load this file

l = np.load('test1.npy')
print(l)

# now im going to save multiple arrays, for which i use savez function
# You save multiple arrays in an uncompressed archive using np.savez and passing the arrays as keyword arguments:
np.savez('test2.npz',a=x,b=y) # a = key, x = value | b = key , y = value dict = ['a':x , 'b':y ]
# now im going to load this file, When loading an .npz file, you get back a dict-like object that loads the individual
# arrays lazily:
l = np.load('test2.npz') 
print(l) # npz file object
print(l['a'])
print(l['b'])


# # Numpy - Linear Algebra

# In[92]:


# Linear algebra, like matrix multiplication, decompositions, determinants, and other
# square matrix math, is an important part of any array library. Unlike some languages
# like MATLAB, multiplying two two-dimensional arrays with * is an element-wise
# product instead of a matrix dot product. Thus, there is a function dot, both an array
# method and a function in the numpy namespace, for matrix multiplication:

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a*b) # * will mutiply two matrices element by element 

# To find the dot product of two arrays.
a = 2
b = 3
print(np.dot(a,b))

# 1-D
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(np.dot(a,b)) # a.dot(b) is equivalent to np.dot(a, b):


# 2-D
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(a)
print(b)
# here multiplication works as same as we did, (PS: column1== row2)
# [1 2 3]   [ 7  8]
# [4 5 6] x [ 9 10]
#           [11 12]
print(a.dot(b))

# A matrix product between a two-dimensional array and a suitably sized onedimensional array results in a one-dimensional array:
x = np.array([[1., 2., 3.], [4., 5., 6.]])
print(np.dot(x, np.ones(3)))

# The @ symbol (as of Python 3.5) also works as an infix operator that performs matrix multiplication:
print(x @ np.ones(3))

# numpy.linalg has a standard set of matrix decompositions and things like inverse
# and determinant. These are implemented under the hood via the same industrystandard linear algebra libraries used in
# other languages like MATLAB and R, such as BLAS, LAPACK, or possibly (depending on your NumPy build) the proprietary Intel
# MKL (Math Kernel Library):
# linalg = linear algebra
from numpy.linalg import *
arr = np.arange(4).reshape(2,2)
print(arr)
arr1 = np.arange(25).reshape(5,5)
print(arr1)
# # to find determinant of a matrix , we can use det function of linalg module
# print(det(arr))
print(det(arr1))
# print(inv(arr1)) # this will cause error because the determinant of arr1 is 0 , inv(A)= adj(A)/|A|
# now we find inv of that array whose det is not zero
arr = np.random.randn(5,5)
print(det(arr))
print(inv(arr))

# another function diag, which return the diagonal elements of an array in form of 1-D array.
arr1 = np.arange(25).reshape(5,5)
print(arr1)
print(np.diag(arr1))

# an other use of diagonal matrix is that we can passan array of values in diag function and the function will set all the
# given values as diagonal and will set rest of the to zero
arr = np.array([2,4,6,8,10])
print(np.diag(arr))

# another function trace, which Compute the sum of the diagonal elements.
arr1 = np.arange(25).reshape(5,5)
print(arr1)
print(np.trace(arr1))

# See Table 4-7 for a full listing of functions. (visit Python for Aata Analysis by Wes McKinney book pg. no 117) for Table 4-7


# # Numpy - Pseudorandom Number Generation

# In[106]:


# The numpy.random module supplements the built-in Python random with functions
# for efficiently generating whole arrays of sample values from many kinds of probabil‐
# ity distributions

# the main function of numpy.random module is seed() function which initialize the random number generator.
np.random.seed(1) # here i initialized seed to 1
# now i can use any function of Numpy for generating random numbers and now on for every function seed value is 1 untill i 
# change its value, if i forget to set its value then the default value of seed function is my current time.
# setting a particular value of seed can help us generating same random numbers ever and ever again. if i want complete random
# numbers i just need to remove initialization line of seed


''' A good source to know about seed function is, [https://www.sharpsightlabs.com/blog/numpy-random-seed/]'''

# a function called np.random.normal() draw samples from a normal (Gaussian) distribution.
arr = np.random.normal(size=(5,5))
print(arr)

# a function called np.random.randint() draw random integers from a given low-to-high range.
# randint's first parameter considered as inclusive(means it can be included in the array returned) and second parameter
# is considered to be exclusive(meas it cannot be included in the array returned).
arr = np.random.randint(0,9,size=10) # this will generate random integers from 0 to 9 with seeding point initialized to 1.
print(arr)

arr = np.random.uniform(0,9,size=10)
print(arr)

# another function shuffle that suffles the elements of an array.
x = np.arange(1,100,5)
print(x)
np.random.shuffle(x)
print(x)


# See Table 4-8 for a full listing of random functions. (visit Python for Aata Analysis by Wes McKinney book pg. no 119)
# for Table 4-8


# # Numpy - Advanced Array Manipulation
# ### Appendix A

# ## Numpy - Reshaping Arrays
# * Gives a new shape to an array without changing its data. 
# * Gives a new shape to an array as well as dimensions.
# * Syntax - numpy.reshape(a, newshape, order='C') 

# In[83]:


# in the array below i have 25 elements and to reshape it i just need to find the factors of 25.
# 25=5x5 (this is the only factor of 25)
arr = np.arange(25)
print(arr)
print(arr.reshape(5,5))

# another method to reshape an array can be,
arr = np.arange(25).reshape(5,5) # this is similar to the above one and handy as well
print(arr)
# last parameter of reshape is order. which defines how an array will going to be look.
# C - order means the array will be a row major array. (By default)
# F - order means the array will be a column major array.
# for visual representation (visit Python for Aata Analysis by Wes McKinney book pg. no 452) for figure A-3


arr = np.arange(25).reshape(5,5,order='C') # row major
print(arr)
arr = np.arange(25).reshape(5,5,order='F') # column major
print(arr)

# some more ex. of reshaping
arr = np.arange(24).reshape(4,6) # factors of 24 are, 24(4,6) , 24(2,2,6) , 24(2,2,3,2)
print(arr)

arr = np.arange(24).reshape(2,2,6)
print(arr)

arr = np.arange(24).reshape(2,2,3,2)
print(arr)

# you'll get an error if you cant fill up the matrix completely.

# print(np.arange(24).reshape(2,2,3)) # here matrix is not comletely filled
# if you want to prevent the error you can put -1 in that position , after which numpy will responsible for mangening this.
# a thing to remember is that we can replace -1 only once like this reshape(n,n,..,-1) if we do this reshape(n,n,..,-1,-1)
# this will cause error.

print(np.arange(24).reshape(2,2,-1)) # here -1 will replace to 6 because thats the only number which will complete the 
# number (2x2x6)
print(np.arange(24).reshape(2,2,3,-1)) # here -1 will replace to 3 because thats the only number which will complete the 
# number (2x2x3x3)


# ## Numpy - Concatenating and Splitting Arrays
# * Concatenate takes a sequence (tuple, list, etc.) of arrays and joins them together in order along the input axis.
# * In order to concatenate two or more arrays the number of dimensions must be same.

# In[196]:


arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
# we can use square braces ans circular braces both to keep arrays as first parameter.
print(np.concatenate([arr1,arr2]))  
print(np.concatenate((arr1,arr2)))
# we can change the axis of concatenation as well, by default it is axis = 0.
print(np.concatenate([arr1,arr2],axis=1))  
print(np.concatenate((arr1,arr2),axis=1))

while concatenating array be carefull about the dimension and shape of an array.
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
a = (2,2)
b = (1,2)
axis(0,1)
print(np.concatenate((a,b))) # here axis is 0 which means the array will concatenate along axis 0(which is concatenating 
axis, (2,1) = 0 axis here) and we always need to check the values of axis other than concatenating axis(0)
and in order to concatenate the values should be same ( (2,2) = axis 1 and values are some ). thats why catenation is 
possible here.
print(np.concatenate((a,b),axis = 1)) # this will cause error because the values of axis other than concatenating axis(1)(
(2,2) = 1 axis here) are not same ( (2,1) = 0 axis here, clearly 2 and 1 are not same). thats why catenation is not 
possible here.
print(np.concatenate((a,b.T),axis = 1)) # here i transposed array b due to which the axis other than concatenating axis has
become equal. 
a = (2,2)
b = (2,1)
axis(0,1)

# There are some convenience functions, like vstack and hstack, for common kinds of concatenation. The preceding operations
# could have been expressed as:
print(np.vstack((arr1, arr2))) # vstack means vertical stack, in which axis is 0
print(np.hstack((arr1, arr2))) # hstack means vertical stack, in which axis is 1

# another function column_stack which take a sequence of 1-D arrays and stack them as columns to make a single 2-D array.
a = np.array((1,2,3))
b = np.array((2,3,4))
print(np.column_stack((a,b)))



# Split, on the other hand, slices apart an array into multiple arrays along an axis:
# arr = np.array([0,1,2,3,4,5,6,7,8])
# print(np.split(arr,3)) # here my arr has 9 elements and amd i have splitted my array into 3 parts.
# print(np.split(arr,(2,4,6))) # this will split at 2,4 and 6 index number.

arr = np.random.randint(1,50,25).reshape(5,5)
print(arr)
print(np.split(arr,(2,3),axis = 1)) # axis 1 represents columns
print(np.split(arr,(2,3),axis = 0)) # axis 0 represents rows

# There are some convenience functions, like vsplit and hsplit, for common kinds of splitting. The preceding operations
# could have been expressed as:
print(np.hsplit(arr,(2,3))) # hsplit means horizontal split
print(np.vsplit(arr,(2,3))) # vsplit means vertical split

# 1) AXIS 0 IS THE DIRECTION ALONG THE ROWS , axis 0 is the axis that runs downward down the rows(which means that any change 
# in axis 0 will apply to column)
# 2) AXIS 1 IS THE DIRECTION ALONG THE COLUMN , axis 1 is the axis that runs horizontally across the columns(which means that
# any change in axis 1 will apply to rows) 


# See Table A-1 for a full listing of concatenating and splitting functions. (visit Python for Aata Analysis by WesMcKinney 
# book pg. no 456) for Table A-1.


# ## Numpy - Stacking helpers: r_ and c_

# In[201]:


# There are two special objects in the NumPy namespace, r_ and c_, that make stacking
# arrays more concise:
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print(np.r_[arr1, arr2])
print(np.c_[arr1,arr2])


# ## Numpy - Repeating Elements: tile and repeat
# * Tile constructs an array by repeating A the number of times given by reps.
# * Syntax - numpy.tile(A, reps)
# * Repeat replicates each element in an array some number of times, producing a larger array.
# * Syntax - numpy.repeat(a, repeats, axis=None)

# In[208]:


# Two useful tools for repeating or replicating arrays to produce larger arrays are the repeat and tile functions. 

# numpy.repeat repeats all the elements of an array according to specified value.
arr = np.array([1,2,3])
print(np.repeat(arr,3)) # here each element will repeat 3 times

# numpy.tile repeats the tile of elements of an array according to specified value.
arr = np.array([1,2,3])
print(np.tile(arr,2)) # here array will repeat 2 tiles.

