'''Convert Key, Values in a Dictionary to List
dict_to_list({
"D": 1,
"B": 2,
"C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
'''


#Creating a dictinary
dict_={
"D": 1,
"B": 2,
"C": 3
}

#Empty list to store items
list_=[]

for i , j in dict_.items():
    list_.append((i,j))

print("Dictinary into list is : ",sorted(list_))