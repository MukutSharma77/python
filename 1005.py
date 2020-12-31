''' Write a Python program to rotate a given list by specified number of items to the right or left direction. Go to the editor
original List:
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 4,'left')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 2,left')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 4,'right')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 2,'right')
Rotate the said list in left direction by 4:
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
Rotate the said list in left direction by 2:
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Rotate the said list in Right direction by 4:
[8, 9, 10, 1, 2, 3, 4, 5, 6]
Rotate the said list in Right direction by 2:
[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]'''


def rotate_lst(list_,num,direction):
    if direction=='left':
        print(list_[num:]+list_[:num])

    else:
        print(list_[-num:] + list_[:-num])

rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 4,'left')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 2,'left')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 4,'right')
rotate_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 2,'right')