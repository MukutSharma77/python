''' Write a Python program to count the number of sublists contain a particular element. Go to the editor
Original list:
[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
check_([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1,7)
Output:
1  is  3  Times
7  is  2  Times

Original list:
[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
check_([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A','E')
A  is  3  Times
E  is  1  Times

'''

def check_(lst,*args):
    list_=list(args)
    for i in list_:
        count=0
        for item in lst:
            for element in item:
                if element==i:
                    count+=1

        print(i, ' is ',count,' Times')




check_([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A','E')
check_([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1,7)