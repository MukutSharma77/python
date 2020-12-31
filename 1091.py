'''Following is the 2-D array. Print max from axis 0 and min from axis 1
import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
Expected Output:
Printing Original array
[[34 43 73]
 [82 22 12]
 [53 94 66]]
Printing amin Of Axis 1
[34 12 53]
Printing amax Of Axis 0
[82 94 73]'''

import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print('Original array : \n',sampleArray)
max_=numpy.amax(sampleArray,0)
min_=numpy.amin(sampleArray,1)
print('Printing amin of Axis 1 :  ',min_)
print('Printing amax of Axis 0 :  ',max_)