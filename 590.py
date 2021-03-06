'''Numbers to Arrays and Vice Versa
Write two functions:
to_list(), which converts a number to a list of its digits.
to_number(), which converts a list of digits back to its number.
Examples
to_list(235) ➞ [2, 3, 5]
to_list(0) ➞ [0]
to_number([2, 3, 5]) ➞ 235
to_number([0]) ➞ 0'''

def to_number(lst):
    lst_=[str(i) for i in lst]
    print(''.join(lst_))

def to_lst(num):
    lst_=[int(i) for i in str(num)]
    print(lst_)

to_number([2,3,5])
to_lst(235)