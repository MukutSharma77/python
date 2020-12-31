'''Flip the Array
Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.
In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.
Examples
flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.
flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# Take a vertical list and flip it horizontal.
flip_list([]) ➞ []
'''

def flip_list(lst):
    output_lst=[]
    for i in lst:
        if type(i)==list:
            for j in i:
                output_lst.append(j)

        else:
            sub_=[]
            sub_.append(i)
            output_lst.append(sub_)

    print(output_lst)


flip_list([1, 2, 3, 4])
flip_list([[5], [6], [9]])
flip_list([])

