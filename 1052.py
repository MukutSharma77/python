'''Write a Python program to get the index of the first element which is greater than a specified element. Go to the editor
Original list:
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 73 )
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 21 )
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 80
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 55 )
Output:
4
1
5
3'''

def first_largest(lst , num):
    for i in range(len(lst)):
        if lst[i] > num:
            print(i)
            break


first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 73 )
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 21 )
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 80 )
first_largest( [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83] , 55 )
