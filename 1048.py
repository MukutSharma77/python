'''Write a Python program to add two given lists of different lengths, start from left.
add_( [2, 4, 7, 0, 5, 8] , [3, 3, -1, 7] )
add_( [1, 2, 3, 4, 5, 6] , [2, 4, -3] )
output:
[5, 7, 6, 7, 5, 8]
[3, 6, 0, 4, 5, 6]'''

def add_(lst1 , lst2):
    output=[]
    for i in range(len(lst2)):
        output.append(lst1[i] + lst2[i])

    print(output+lst1[len(lst2) :])

add_( [2, 4, 7, 0, 5, 8] , [3, 3, -1, 7] )
add_( [1, 2, 3, 4, 5, 6] , [2, 4, -3] )
