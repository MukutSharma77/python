'''Write a Python program to find the nested lists elements which are present in another list.
lst_present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  , [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]] )
Output :
Intersection of said nested lists:
[[12], [7, 11], [1, 5, 8]]'''

def lst_present(lst1 , lst2):
    lst_output=[]
    for i in lst2:
        lsting=[ ]
        for j in i:
            if j in  lst1:
                lsting.append(j)
        lst_output.append(lsting)

    print(lst_output)

lst_present([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  , [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]] )