'''Following is the input NumPy array delete column two and insert following new column in its place.
import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = numpy.array([[10,10,10]])
Expected Output:
Printing Original array
[[34 43 73]
 [82 22 12]
 [53 94 66]]
Array after deleting column 2 on axis 1
[[34 73]
 [82 12]
 [53 66]]
Array after inserting column 2 on axis 1
[[34 10 73]
 [82 10 12]
 [53 10 66]]'''


import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = numpy.array([[10,10,10]])
print("Original Array is :   \n",sampleArray)


dlt_col2=numpy.delete(sampleArray,1,axis=1)
print('\nAfter removing second column : \n ',dlt_col2)

insert_col2=numpy.insert(dlt_col2,1,newColumn,axis=1)
print('\nAfter removing second column :  \n',insert_col2)
