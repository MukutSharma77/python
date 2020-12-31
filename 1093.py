'''
Write a NumPy program to test whether none of the elements of a given array is zero.
check_0( [1 2 3 4] )
check_0( [0 1 2 3] )
True
False     '''
import numpy

def check_0(arr):
    print(numpy.all(arr))

check_0( [1 ,2 ,3, 4] )
check_0( [0 ,1 ,2 ,3] )
