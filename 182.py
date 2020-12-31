'''The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended.
 Can you fix the code?
Examples
clone([1, 1]) ➞ [1, 1, [1, 1]]'''


#Inputing list
list_=['a','b']

# Copying list
list2=list_.copy()

#appending list in list2
list2.append(list_)

print(list2)