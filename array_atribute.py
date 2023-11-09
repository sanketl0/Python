# attributes of array

import numpy as arr
aa=arr.array([1,2,3,4,5,6,7,8,9])
ar=arr.array([[1,2,3],[5,6,4]])
print("single array:",aa)
print("multirow array:",ar)

print("which type of matrix are given dimentional:",aa.ndim)
print("which type of matrix are given dimentional:",ar.ndim)

print("shape of array:",aa.shape)
print("shape of array:",ar.shape)

print("datatype of array:",aa.dtype)
print("datatype of array:",ar.dtype)

print("size of array:",aa.size)
print("size of array:",ar.size)

print("itme size of array:",aa.itemsize)
print("itme size of array:",ar.itemsize)

print('memory taken by each value:',aa.nbytes)
print('memory taken by each value:',ar.nbytes)

# we can convert one dimentional array into two dimentional array 
    # with the help of reshape() method