#!/usr/bin/env python
# coding: utf-8

# # Pandas
# * Developer **Wes McKinney** started working on **Pandas** in 2008.
# * Pandas contains data structures and data manipulation tools designed to make **Data Cleaning** and **Analysis** fast and easy in Python. 
# * Pandas is often used in tandem with numerical computing tools like NumPy and SciPy, analytical libraries like statsmodels and scikit-learn, and data visualization libraries like matplotlib.
# * Pandas adopts significant parts of NumPy’s idiomatic style of array-based computing, especially array-based functions and a preference for data processing without for loops.
# * While pandas adopts many coding idioms from NumPy, the biggest difference is that pandas is designed for working with tabular or heterogeneous data.
# * NumPy, by contrast, is best suited for working with homogeneous numerical array data.

# In[131]:


import pandas as pd 
# here pd is just the alias for pandas means that i can use pd instead of pandas. But when i need to import something from pandas
# i will have to use pandas instead of pd.


# In[132]:


from pandas import Series ,DataFrame


# In[133]:


import numpy as np


# # Introduction to Pandas Data Structures
# 
# * To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame.  While they are not a universal solution for every problem, they provide a solid, easy-to-use basis for most applications.
# 

# ## Pandas - Series
# * A Series is a one-dimensional array-like object containing a sequence of values (of similar types to NumPy types) 
# * It also contains an associated array of data labels, called its index.
# * Simply, Series is a combination of Values and Index(labels).
# * The Series data must be one-dimentional data. For this purpose we later be using DataFrame.
# * Syntax - pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
# 
# **Source for series data**
# * Python list
# * Numpy array
# * Python dictionary

# In[157]:


# The simplest Series is formed from only an array of data:
ser = pd.Series([1,2,3,4])
print(ser)
# in the output the numbers on the left are the index numbers and the numbers on the right are the values of the Series.
# Since we did not specify an index for the data, a default one consisting of the integers 0 through N - 1 (where N is the
# length of the data) is created.

# You can get the array representation and index object of the Series via. its values and index attributes, respectively.
print(ser.values) # for values
print(ser.index) # for index

# Often it will be desirable to create a Series with an index identifying each data point with a label: which means that you
# can change the index value as your wish.
# here index can contain values of multiple data types. like, index = ['a','b','c',0,1,True]
ser = pd.Series([1,2,3,4,5],index=['b','i','l','a','l'])
print(ser)
print(ser.index) # the dtype of this index is 'object' dtype, if data seems complex to pandas it will change it dtype to 'object'.

# Compared with NumPy arrays, you can use labels in the index when selecting single values or a set of values.
print(ser['b']) # we can use index number as well, like this ser[0] this will return the same element. which means that 
# changing index values doesnt change the real integer values of index number, we can use it if we want to.
print(ser['l'])
# we can also extract multiple values just as we do in numpy via fancy indexing.
# print(ser[['b','a','i']])

# we can also change the index of a series like this(but cant set values like this,
ser.index = ['B','I','L','A','L']
print(ser)
# Using NumPy functions or NumPy-like operations, such as filtering with a boolean array, scalar multiplication, or applying 
# math functions, will preserve the index-value link:
print(ser[ser>1])
print(ser*2) # this will not append changes in ser , to store the change in ser we can assign the result in it.

# Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values.
# It can be used in many contexts where you might use a dict:
print('a' in ser)
print('l' in ser)
print('o' in ser)

# Should you have data contained in a Python dict, you can create a Series from it by passing the dict:
# We can use this method if we have a file which containing data in form of dictionary.
city = { 'Karachi':3780 , 
        'Lahore':1772 ,
        'Mianwali':5840 , 
        'Hyderabad':292 }
city0 = pd.Series(city)
print(city0)
# When you are only passing a dict, the index in the resulting Series will have the dict’s keys in sorted order.
# You can override this by passing the dict keys in the order you want them to appear in the resulting Series:
ch_cities = ['Lahore','Karachi','Mianwali','KPK'] 
city1 = pd.Series(city,index=ch_cities) # this will just change the position of index in the series , the values always remain
# constant. This will help us if the values of our dictionary are not in our required arrangement we can arrange the values in 
# by changing index arragement.
print(city1)
# Here, three values found in ch_cities were placed in the appropriate locations, but since
# no value for 'KPK' was found, it appears as NaN (not a number), which is considered in pandas to mark missing or NA?(None)
# values. Since 'Hyderabad' was not included in ch_cities, it is excluded from the resulting object.
# NaN value means, value doesnot exist in pandas series. and NaN is extremely not equal to zero.

# # The isnull and notnull functions in pandas should be used to detect missing data:
print(pd.isnull(city1)) # here KPK is null becuase this has no value , another syntax is city.isnull()
print(pd.notnull(city1)) # here all the keys except KPK are not null , another syntax is city.notnull

# A useful Series feature for many applications is that it automatically aligns by index label in arithmetic operations:
print(city0)
print(city1)
print(city0+city1) # here you'll see that after addition of city0 and city1 Hyderabad will be having NaN value instead it has
# 5000 in city0 series, a thing to remeber is that any if a series doesn't have the value on the same index number which another
# city will be having on the same index number then any arithimetic operation will return NaN to that value.
# Any_value + NaN = Nan, # Any_value * NaN = Nan , # Any_value - NaN = Nan, # Any_value / NaN = Nan

# we can also name the series with the help of name keyword in Series, which we can be used as column header when we will apply
# data frame of it.
sales = pd.Series([100,200,300,400],index = ['Jan','Feb','March','April'],name = 'Company Sales') # here i have named my sales
# series to 'Company Sales'
print(sales)
# we can also name the index object of a series, with the help of this syntax, series-name.index.name = 'any_name' , which later
# can be used as column header when we will apply data frame of it.
# sales.index.name = 'Months'
print(sales)

# Creata a pandas series to store a Canteen data to hold values of how many sandwiches are sold in a week.
sandw = pd.Series([50,60,70,80,90,100,0],index = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],name = 'Canteen Sandwiches')
sandw.index.name = 'Days'
print(sandw)

# we can also use numpy array for creating serise.
arr = np.array([1,2,3,4,5,6,7])
day = np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
numpd = pd.Series(arr,day)
print(numpd)


# ## Pandas - DataFrame
# * A DataFrame represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type (numeric, string,boolean, etc). 
# * To be precise DataFrame is a bundle of multiple Series.
# * The DataFrame has both a row and column index; it can be thought of as a dict of Series all sharing the same index.
# * Under the hood, the data is stored as one or more two-dimensional blocks rather than a list, dict, or some other collection of one-dimensional arrays.
# * Syntax - pd.DataFrame(
#     data=None,
#     index: Union[Collection, NoneType] = None,
#     columns: Union[Collection, NoneType] = None,
#     dtype: Union[str, numpy.dtype, ForwardRef('ExtensionDtype'), NoneType] = None,
#     copy: bool = False,
#     }

# In[153]:


# There are many ways to construct a DataFrame, though one of the most common is from a dict of equal-length lists
# or NumPy arrays:
data = { 'cities':['Karachi','Lahore','Bani Gala','Murry','Skardu','Kashmir'] , 
         'year':[2000,2001,2002,2003,2004,2005] ,
         'population':['2M','2.5M','1.5M','1M','0.5M','0.2M'] }
dframe = pd.DataFrame(data)
print(dframe) #  The resulting DataFrame will have its index assigned automatically as with Series, and the columns are placed 
# in sorted order, here keys are used as columns label and values are used as values.

# For large DataFrames, the head method selects only the first five rows:
print(dframe.head())

# If you specify a sequence of columns, the DataFrame’s columns will be arranged in that order:
dframe = pd.DataFrame(data , columns = ['year','population','cities'])
print(dframe)

a = pd.Series(['P','T','I','A'],name = 'Country')
print(pd.DataFrame(a))
# we can also create a DataFrame by using Series and the Series' name will be used as column name in the DataFrame

# we can pass series like this way also,
# # Series by array
names_arr = np.array([200,300,400,500,600])
fs = pd.Series(names_arr ,name = 'Muslim ') 
fs.index = ['Pakistan','Turkey','Saudia','Indonesia','Italy']
print(fs)

oic = { 'Tur':200,'Sau':12,'Ind':45454,'Ita':5,'Pakistan':5}
s = pd.Series(oic,name = 'Mus')
print(s)

fd = pd.DataFrame(data = [fs,s])
print(fd)

# to access columns we just need to use 'columns' attribute.
print(dframe.columns)

# If you pass a column that isn’t contained in the dict, it will appear with missing values (NaN) in the result:
dframe = pd.DataFrame(data , columns = ['year','population','cities','Budget'])
print(dframe)

# we can also change the index object, by using index keyword argument of DataFrame.
dframe = pd.DataFrame(data , 
                      columns = ['year','population','cities','budget'],
                      index = ['one', 'two', 'three', 'four','five','six'])
print(dframe)

# A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:
print(dframe['year']) # if we want to get multiple Series we can surely use fancy indexing and pass multiple labels in it.
# if we pass some labels that are not the part of our DataFrame we'll get an error.
print(dframe[['cities','year']])
# another way to access a series.
print(dframe.cities)
# Note that the returned Series have the same index as the DataFrame, and their name attribute has been appropriately set.

# Attribute-like access (e.g., dframe.year) and tab completion of column names in IPython is provided as a convenience.
# frame2[column] works for any column name, but dframe.column only works when the column name is a valid Python variable name.
# suppose that if our city name was '1cities' then we can access it easily with the help of single  bracket notation but
# we can't access it by using dframe.1cities, we'll get error.

# Rows can also be retrieved by position or name with the special loc attribute.
print(dframe.loc['three']) # if we want to get multiple indexes we can surely use fancy indexing and pass multiple indexes in it.
# if we pass some indexes that are not the part of our DataFrame it will set all the values of this to NaN and later can cuase 
# problem. so better not to do it.
print(dframe.loc[['four','five']])

# Columns can be modified by assignment. For example, the empty 'budget' column could be assigned a scalar value or an array
# of values:
dframe['budget'] = 0 # this will set all the values to zero
print(dframe)
# we can also set the values using range function, wether of Python or of Numpy
dframe['budget'] = range(6)
print(dframe)

# When you are assigning lists or arrays to a column, the value’s length must match the length of the DataFrame. If you 
# assign a Series, its labels will be realigned exactly to the DataFrame’s index, inserting missing values in any holes:
dframe['budget'] = [2,4,6,8,10,12] # if it was [2,4,6,8] , which means the len of list is not equivalent of the DataFrame's 
print(dframe)
# value len, it will cause error.
# we can also use Series for this,
val = pd.Series(['1.94B','0.5B','0.9B'],index = ['one','three','five'])
dframe['budget'] = val
print(dframe)

# Assigning a column that doesn’t exist will create a new column. The del keyword will delete columns as with a dict.
# New columns cannot be created with the frame2.eastern syntax.
dframe['ncities'] = dframe.cities == 'Karachi'
print(dframe)

# As an example of del, I first add a new column of boolean values where the cities column equals 'Karachi':
print(dframe.columns)
del dframe['ncities']
print(dframe)
print(dframe.columns)
# The column returned from indexing a DataFrame is a view on the underlying data, not a copy. Thus, any in-place modifications
# to the Series will be reflected in the DataFrame. The columncan beexplicitly copied with the Series’s copy method.

# Another common form of data is a nested dict of dicts:
population = { 'Karachi':{ 2000:'2M',2001:'4M' } , 
               'Lahore':{ 2001:'2.5M' , 2003:'3.5M' , 2004:'1.5'} }
df = pd.DataFrame(population)
print(df)

# You can transpose the DataFrame (swap rows and columns) with similar syntax to a NumPy array:
print(df.T)

# The keys in the inner dicts are combined and sorted to form the index in the result.
# This above statement will become false if an explicit index is specified:
df1 = pd.DataFrame(population , index = [2001,2003,2004])
print(df1)

# Dicts of Series are treated in much the same way.
k_v = pd.Series(['2M','4M'],index = [2000,2001])
l_v = pd.Series(['2.5M','3.5M','1.5'],index = [2001,2003,2004])
pop = { 'Karachi':k_v , 'Lahore':l_v }
df_pop = pd.DataFrame(pop)
print(df_pop)
# ___________________ OR ____________________ 
pop = { 'Karachi':df['Karachi'] , 'Lahore':df['Lahore'] }
pop_df = pd.DataFrame(pop)
print(pop_df)

# If a DataFrame’s index and columns have their name attributes set, these will also be displayed:
dframe.index.name = 'S. No' 
dframe.columns.name = 'Essentials' 
print(dframe)

# As with Series, the values attribute returns the data contained in the DataFrame as a two-dimensional ndarray:
print(dframe.values)
      
# If the DataFrame’s columns are different dtypes, the dtype of the values array will be chosen to accommodate all
# of the columns:
print(dframe.values.dtype)

# to get more information on in how many times data can be given to DataFrame, 
# Visit table 5-1 Python For Data Analysis By Wes Mckinney book pg # 134


# ## Pandas - Index Objects
# * Pandas’s Index objects are responsible for holding the axis labels and other metadata (like the axis name or names).
# * Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index.
# * Syntax - pandas.Index(data=None, dtype=None, copy=False, name=None, tupleize_cols=True, **kwargs)

# In[304]:


srz = pd.Series(['Pakistan','Turkey','Iran','Saudia'],index = ['f','s','t','f'])
print(srz)
Index = srz.index
print(Index)
print(Index[2:])
# Index objects are immutable and thus can’t be modified by the user:
# Index[1] = 'second'# this will cause error since index objects are immutable , we cant change them

# # Immutability makes it safer to share Index objects among data structures:
labels = pd.Index(np.arange(4)) # pd.Index will return an immutable object. 
sa = pd.Series(['Pakistan','Turkey','Iran','Saudia'],index = labels)
print(sa)
# # checking
print(sa.index is labels)

# In addition to being array-like, an Index also behaves like a fixed-size set(we called it a set like because this has methods
# of set):
print(dframe.columns)
print('year' in dframe.columns) 

# Unlike Python sets, a pandas Index can contain duplicate labels:
dub_labels = pd.Index(['Pakistan','Turkey','Pakistan','Turkey','Russia','Iran'])
print(dub_labels)
print(dub_labels[0]) # we can use indexing here because its an array also and a set as well.

# Selections with duplicate labels will select all occurrences of that label.
dfn = pd.DataFrame(['2M','2.5M','1.5M','1M','0.5M','0.2M'],index = dub_labels )
dfn.index.name = 'Countries'
print(dfn)
print(dfn.loc['Pakistan'])

# append
d1 = pd.Index(['Uganda','Wakanda','Mississippi'])
dub = dub_labels.append(d1) # this will concatenate both the index object.
print(dub)
# difference 
print(dub_labels.difference(d1)) # this will Return a new Index with elements from the index that are not in `other`.
# isin
print(d1.isin(['Pakistan','Wakanda']))
print(d1.isin(['Pakistan','Wakanda','Uganda'])) # Compute boolean array indicating whether each value is contained in 
# the passed collection
# delete
a = dub.delete(-1) # this will create new index by deleting that element on that index number we have passed 
print(a)
# Visit table 5-2 Python For Data Analysis By Wes Mckinney book pg # 136


# # Essential Functionality
# * This section will walk you through the fundamental mechanics of interacting with the data contained in a Series or DataFrame.

# ## Pandas - Reindexing
# * An important method on pandas objects is reindex, which means to create a new object with the data conformed to a new index.

# In[387]:


ns = pd.Series(['Wasay','Abubakar','Rabiyan','Zaroon'],index = ['d','b','c','a'])
print(ns)
ns = ns.reindex(['a','b','c','d','e']) # ns.index = ['a','b','c','d','e'] this will cause error becuase 'e' is an extra index 
# # number here. but reindex tackels this problem and set the value of this to NaN.
print(ns)

# For ordered data like time series, it may be desirable to do some interpolation or filling of values when reindexing. The
# method option allows us to do this, using a method such as ffill, which forward-fills the values:
color = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(color)
print(color.reindex(range(6)))
print(color.reindex(range(6),method='ffill')) # here the NaN value will be filled by its prior index value.

# With DataFrame, reindex can alter either the (row) index, columns, or both. When passed only a sequence, it reindexes 
# the rows in the result:
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                      index=['a', 'c', 'd'],
                      columns=['Ohio', 'Texas', 'California'])
frame = frame.reindex(['a','b','c','d'])
print(frame)
# The columns can be reindexed with the columns keyword
print(frame.reindex(columns = ['Ohio','Washington Dc','California'],fill_value = 999))
frame = frame.reindex(columns = ['Ohio','Washington Dc','California'])
print(frame)
# the first parameter of reindex is 'labels' in which we can pass the labels of either for index or for columns by using
# axis parameter. but the second method is 'index' in which we can only index values and we cant use axis parameter for this,
# else-wise this will cause error.

# For more reindex function arguments Visit table 5-3 Python For Data Analysis By Wes Mckinney book pg # 138


# ## Pandas - Dropping Entries from an Axis
# * The **drop method** will return a new object with the indicated value or values deleted from an axis:

# In[400]:


# for Series
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

new = obj.drop('d')
print(new)

new1 = obj.drop(['a','e'])
print(new1)

# for DataFrame
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# Calling drop with a sequence of labels will drop values from the row labels (axis 0):
data1 = data.drop('Ohio') # by default the value or axis is none or 0.
print(data1)
# You can drop values from the columns by passing axis=1 or axis='columns':
data2 = data.drop('three',axis = 1)
print(data2)
data3 = data.drop(['two','four'],axis = 1)
print(data3)

# Many functions, like drop, which modify the size or shape of a Series or DataFrame,
# can manipulate an object in-place without returning a new object:

data.drop(['two','four'],axis = 1,inplace = True)
print(data) # Be careful with the inplace, as it destroys any data that is dropped.


# ## Pandas - Indexing, Selection, and Filtering

# In[559]:


# Series indexing (obj[...]) works analogously to NumPy array indexing, except you
# can use the Series’s index values instead of only integers. Here are some examples of this:
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b'])
print(obj[1])
print(obj[[0,3,1]]) # can also do this using labels
print(obj[1:4])
print(obj[obj>1]) # boolean indexing
# Slicing with labels behaves differently than normal Python slicing in that the end‐point is inclusive
print(obj['b':'d'])

# Indexing into a DataFrame is for retrieving one or more columns either with a single value or sequence
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

print(data)
print(data['three'])
print(data[data.columns[[0,2]]]) # we can also use index number of columns
print(data[['one','three']]) # we can either select 1 column or multiple columns with the help of fancy indexing.
# Indexing like this has a few special cases. First, slicing or selecting data with a boolean array:
print(data[1:]) # we can do slicing here, but we cant select multiple indexes here. for which we have loc function
print(data[data['two']>=5])
# The row selection syntax data[:2] is provided as a convenience. Passing a single element or a list to the [] 
# operator selects columns.

# Another use case is in indexing with a boolean DataFrame, such as one produced by a scalar comparison:
print(data>4)
print()
data[data>4] = 0
print()
print(data)

######### Selection with loc and iloc #########
# For DataFrame label-indexing on the rows, Pandas introduce the special indexing operators
# loc and iloc. They enable you to select a subset of the rows and columns from a
# DataFrame with NumPy-like notation using either axis labels (loc) or integers (iloc).
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# As a preliminary example, let’s select a single row and multiple columns by label:
print(data.loc['Ohio','two']) # for single
print()
print(data.loc['Ohio',['two','three']]) # for multiple , we can select multiple rows as well by using fancy indexing

# We’ll then perform some similar selections with integers using iloc:
print(data.iloc[0,1])
print()
print(data.iloc[0,[1,2]])
print()
print(data.iloc[[1,3],[0,-1]])

# Both indexing functions work with slices in addition to single labels or lists of labels:
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data.loc[:'Utah','three'])
print()
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print()
print(data.iloc[:, :3][data.two > 5]) # [data.two > 5] will not select elements of only 'two' column but for all columns 

# For more Indexing options with DataFrame Visit table 5-4 Python For Data Analysis By Wes Mckinney book pg # 144


# ## Pandas - Integer Indexes

# In[660]:


# # Working with pandas objects indexed by integers is something that often trips up
# # new users due to some differences with indexing semantics on built-in Python data
# # structures like lists and tuples. For example, you might not expect the following code
# # to generate an error:
ser = pd.Series(np.arange(3.))
print(ser)
# # ser[-1] this will cause error 
# # a thing to remember is that, we can only use +ve and -ve indexing when the index labels are of string dtype.
ser2 = pd.Series(np.arange(3.),['a','b','c'])
print(ser2[1])
print(ser2[-2])
print(ser2['b'])
# # To keep things consistent, if you have an axis index containing integers, data selection will always be label-oriented(which
# # means we always need to use labels of index).

# For more precise handling or rows and columns, use loc (for labels) or iloc (for integers)


# ## Pandas - Arithmetic and Data Alignment

# In[661]:


# An important pandas feature for some applications is the behavior of arithmetic
# between objects with different indexes. When you are adding together objects, if any
# index pairs are not the same, the respective index in the result will be the union of the
# index pairs
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
# Adding these together yields:
print(s1+s2)
# The internal data alignment introduces missing values in the label locations that don’t
# overlap. Missing values will then propagate in further arithmetic computations.

# In the case of DataFrame, alignment is performed on both the rows and the columns:
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
# # Adding these together returns a DataFrame whose index and columns are the unions of the ones in each DataFrame:
print(df1+df2)
# Since the 'c' and 'e' columns are not found in both DataFrame objects, they appear
# as all missing in the result. The same holds for the rows whose labels are not common to both objects

# If you add DataFrame objects with no column or row labels in common, the result will contain all nulls:
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print()
print(df2)
print(df1+df2)


# ## Pandas - Arithmetic methods with fill values

# In[662]:


df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)
# Adding these together results in NA values in the locations that don’t overlap:
print(df1 + df2)
# Using the add method on df1, I pass df2 and an argument to fill_value:
print(df1.add(df2,fill_value = 0)) # this will set my all values of Nan to 0, Nan = 0 , after which this will add my both DataFrames.
# Nan + value = Nan ,  but , Nan = 0, so , 0 + value = value

# for subtraction 
print(df1.sub(df2,fill_value = 0))
# methods with 'r' included are reverse of what we did above. 
print(df1.rsub(df2,fill_value = 0))

# See Table 5-5 for a listing of Series and DataFrame methods for arithmetic.
# Visit table 5-5 Python For Data Analysis By Wes Mckinney book pg # 149


# ## Pandas - Operations between DataFrame and Series

# In[733]:


# As with NumPy arrays of different dimensions, arithmetic between DataFrame and
# Series is also defined. First, as a motivating example, consider the difference between
# a two-dimensional array and one of its rows:
arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr-arr[0])
# When we subtract arr[0] from arr, the subtraction is performed once for each row. This is referred to as broadcasting which we
# have learned in Numpy.

# Operations between a DataFrame and a Series are similar:
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)
# By default, arithmetic between DataFrame and Series matches the index of the Series
# on the DataFrame’s columns, broadcasting down the rows:
print(frame - series) # bu default this will broadcast down the rows.
# If an index value is not found in either the DataFrame’s columns or the Series’s index,
# the objects will be reindexed to form the union:
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)

# If you want to instead broadcast over the columns, matching on the rows, you have to
# use one of the arithmetic methods. For example:
series3 = frame['d']
print(frame.sub(series3, axis = 'index'))
# The axis number that you pass is the axis to match on. In this case we mean to match
# on the DataFrame’s row index (axis='index' or axis=0) and broadcast across.


# ## Pandas - Function Application and Mapping

# In[781]:


# frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# print(frame)
# print(np.abs(frame)) # abs function will return the distance of each element of an array from zero.

# Another frequent operation is applying a function on one-dimensional arrays to each
# column or row. DataFrame’s apply method does exactly this:
frame = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
f = lambda x : x.max() - x.min()
print(frame.apply(f,axis = 'index')) # here axis is 0(be default) or we can also mention axis = 'index'
print(frame.apply(f,axis='columns')) # here we can mention axis = 1 , which is a same thing.

# Many of the most common array statistics (like sum and mean) are DataFrame methods, so using apply is not necessary.

# The function passed to apply need not return a scalar value; it can also return a Series with multiple values:
print(frame)
def f(x):
#     print(x)
    return pd.Series([x.min(), x.max()], index=['min', 'max']) # this will find the min and max from axis mentioned,
# and return a series of min and max. 
print(frame.apply(f)) # here at axis = 0 , means we are selecting columns one by one b,d,e and  function is returning min
# and max value from b,d and e respectively. since we are using columns so they are used as labels of column and series index
# that we have defined in funtion above, will be the index of new DF.
print(frame.apply(f,axis=1)) # here at axis = 1 , means we are selecting rows one by one Utah,Ohio,Texas,Oregon and  function
# is returning min and max value from Utah,Ohio,Texas,Oregon respectively. since we are using rows so they are used as labels 
# of rows and series index that we have defined in funtion above, will be the column label of new DF. 

# Element-wise Python functions can be used, too. Suppose you wanted to compute a
# formatted string from each floating-point value in frame. You can do this with apply map:
# frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
format = lambda x : ('%.2f' % x) # here f is used for float formatting and 2 is defining how many digits we want after -
# decimal point
print(frame.applymap(format))

frame = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
format = lambda x : (f'Hello {x}')
print(frame.applymap(format))

# The reason for the name applymap is that Series has a map method for applying an element-wise function:
print(frame['e'].map(format))


# ## Pandas - Sorting and Ranking

# In[785]:


# # Sorting a dataset by some criterion is another important built-in operation. To sort
# # lexicographically by row or column index, use the sort_index method, which returns a new, sorted object:
# obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
# print(obj.sort_index())

# # With a DataFrame, you can sort by index on either axis:
# # sorting will also apply on index values
# frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
# print(frame)
# print(frame.sort_index(0))
# print(frame.sort_index(1)) 
# # The data of index is sorted in ascending order by default, but can be sorted in descending order, too:
# print(frame.sort_index(0,ascending = False)) 
# print(frame.sort_index(1,ascending = False)) 

# To sort a Series by its values, use its sort_values method:
obj = pd.Series([4, 7, -3, 2])
print(obj)
print(obj.sort_values())

# Any missing values are sorted to the end of the Series by default:
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())
# When sorting a DataFrame, you can use the data in one or more columns as the sort
# keys. To do so, pass one or more column names to the by option of sort_values:
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by = 'b')) # this will sort 'b'
# To sort by multiple columns, pass a list of names:
print(frame.sort_values(by = ['a','b']))


# # Pandas - Summarizing and Computing Descriptive Statistics

# In[799]:


df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],[np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])
print(df)
# Calling DataFrame’s sum method returns a Series containing column sums:
print(df.sum()) # here by default axis = 0 we can also use axis = 'index' 
# Passing axis='columns' or axis=1 sums across the columns instead:
print(df.sum(axis='columns',skipna = True)) # skipna(True) will skip nan values or set it to zero, by default it is True.
print(df.sum(axis='columns',skipna = False)) # here we set skipna to False thats why its not considering nan 0

# See Table 5-8 for a full list of summary statistics and related methods.
# Visit table 5-8 Python For Data Analysis By Wes Mckinney book pg # 160


# In[ ]:




