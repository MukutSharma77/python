'''Write a Python program to remove a specified column from a given nested list. Go to the editor
Original Nested list:
list_dlt([[1, 2, 3], [2, 4, 5], [1, 1, 1]] , 1)
list_dlt([[1, 2, 3], [-2, 4, -5], [1, -1, 1]] ,  3)
Output:
[[2, 3], [4, 5], [1, 1]]
[[1, 2], [-2, 4], [1, -1]]'''

def list_dlt(lst_,dlt):
    list_output=[ ]
    for i in lst_:
        lst=[]
        for j in range(len(i)):
            if j==dlt-1:
                pass
            else:
                lst.append(i[j])
        list_output.append(lst)

    print(list_output)
list_dlt([[1, 2, 3], [2, 4, 5], [1, 1, 1]] , 1)
list_dlt([[1, 2, 3], [-2, 4, -5], [1, -1, 1]] ,  3)