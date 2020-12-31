'''An Introduction to the Map-Reduce Pattern
You will be implementing a basic case of the map-reduce pattern in programming. Given a vector stored as a list of integers, find the magnitude of the vector. Use the standard distance formula for n-dimensional Cartesian coordinates.
Examples
magnitude([3, 4]) ➞ 5
magnitude([0, 0, -10]) ➞ 10
magnitude([]) ➞ 0
magnitude([2, 3, 6, 1, 8] ) ➞ 10.677078252031311'''

lst=[2, 3, 6, 1, 8]
lst2=[x**2 for x in lst]
print(sum(lst2)**0.5)