'''Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''

lst_=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
lst_output=[]

for i in lst_:
    if type(i)==tuple and len(i) > 0:
        lst_output.append(i)
    elif type(i)==str:
        lst_output.append(i)

print(lst_output)