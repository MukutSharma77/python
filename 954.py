'''Write a Python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]'''



list_= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
lst_output=[]
nth=3
for i in range(0,nth):
    list_loop=[ ]
    for j in range(i,len(list_),nth):
        list_loop.append(list_[j])
    lst_output.append(list_loop)

print(lst_output)