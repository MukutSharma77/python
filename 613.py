'''Let's Sort This List!
Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]
'''

lst=[4, 3, 2, 1]
order=None



if order==None:
    print(lst)

elif order.lower()=='asc':
    print(sorted(lst))

elif order.lower()=='des':
    print(sorted(lst,reverse=True))


else:
    print('Invalid')
