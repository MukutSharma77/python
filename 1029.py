'''Write a Python program to find the difference between two list including duplicate elements.
Original lists:
diff([1, 1, 2, 3, 3, 4, 4, 5, 6, 7]  , [1, 1, 2, 4, 5, 6] )
Output:
Difference between two said list including duplicate elements):
[3, 3, 4, 7]
'''

def diff(list1,list2):
    output=list1
    for i in list2:
        output.remove(i)

    print(output)

diff([1, 1, 2, 3, 3, 4, 4, 5, 6, 7]  , [1, 1, 2, 4, 5, 6] )
