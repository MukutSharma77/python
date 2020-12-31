'''Write a function that converts a dictionary into a list, where each element represents a key-value pair in the form of a list.

Sort the list alphabetically by key.
Examples
to_list({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]'''


#Dictionary
dict_={ "b": 2, "a": 1 }
print("Dictionary is  :   ",dict_)

#Creating empty list
list_=[]

#Appending item in a list and sorting
for i,j in dict_.items():
    list_.append([i,j])
print("List of above dictionary  :   ",list_)

print("Sorted listn  :    ",sorted(list_))
