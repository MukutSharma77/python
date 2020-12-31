'''Following is the provided numPy array. return array of items in the second column from all rows
import numpy
sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
Expected Output:
Printing Input Array
[[11 22 33]
 [44 55 66]
 [77 88 99]]
 Printing array of items in the third column from all rows
[22 55 88]'''


import numpy
sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
lst=[]
for i in sampleArray:
    for j in range(len(i)):
        if j==1:
            lst.append(i[j])

print(lst)