'''Changing Mixed Types
Create a function that changes all the elements in a list as follows:
Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]
change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]'''

lst=[13, "13", "12", "twelve"]
lst2=[]
for i in lst:
    if type(i)==int and i % 2==0:
        lst2.append(i+1)
    elif i == True or i==False:
        lst2.append(not i)

    elif type(i)==str :
        lst2.append(i.title()+'!')

    else:
        lst2.append(i)

print(lst2)