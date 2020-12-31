'''
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

input_lst=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output_lst=[]
for i in range(len(input_lst)):
    if i==0 or i==4 or i==5:
        pass
    else:
        output_lst.append(input_lst[i])


print(output_lst)