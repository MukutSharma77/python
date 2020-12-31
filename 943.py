''' Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350'''

lst=[11, 33, 50]

num=''
for i in lst:
    num+=str(i)

print(int(num))