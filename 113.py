'''Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] new list of comman element from both'''

#Two Given list
list1 =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#appending a common element from both list Using looop to see element of list 1 present in list 2

list_common=[]
for i in list2:
    if i in list1:
        list_common.append(i)

    else:
        pass

print("The comman elements are  :   ",list_common)

if len(list_common) > 0:
    pass
else:
    print("No common charcter")