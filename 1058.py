'''Write a Python program to insert an element in a given list after every nth position. Go to the editor
Original list:
lst_add( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] , 2 , 'a')
lst_add( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] , 4 , 'b')
Output;
[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
[1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]'''

def lst_add(lst , idx , str_):
    lst_output=[]
    for i in range(len(lst)):
        if i==idx:
            lst_output.append(str_)
            idx+=idx
        lst_output.append(lst[i])

    print(lst_output)

    # print(lst)


lst_add( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] , 2 , 'a')
lst_add( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] , 4 , 'b')
