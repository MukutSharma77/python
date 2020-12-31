'''Following is the given numpy array return array of odd rows and even columns
import numpy
sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
Expected Output:
Printing Input Array
[[ 3  6  9 12]
 [15 18 21 24]
 [27 30 33 36]
 [39 42 45 48]
 [51 54 57 60]]
 Printing array of odd rows and even columns
[[ 6 12]
 [30 36]
 [54 60]]'''


import numpy
sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
shape_=sampleArray.shape
row=shape_[0]
col=shape_[1]
mat=[]
for i in range(row):
    lst=[]
    for j in range(col):
        if i%2==0 and j%2!=0:
            # print(sampleArray[i][j])
            lst.append(sampleArray[i][j])

    if lst:
        mat.append(lst)


print(mat)