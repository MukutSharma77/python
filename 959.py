'''959. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]'''

list1=[1, 3, 5, 7, 9, 10]
list2=[2, 4, 6, 8]

for i in range(len(list1)):
    if i==len(list1)-1:
        list1.pop()
        for k in list2:
            list1.append(k)

print(list1)
