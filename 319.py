'''Additive Inverse
A number added with its additive inverse equals zero. Create a function that returns a list of additive inverses.
Examples
additive_inverse([5, -7, 8, 3]) ➞ [-5, 7, -8, -3]
additive_inverse([1, 1, 1, 1, 1]) ➞ [-1, -1, -1, -1, -1]'''



list_=[5, -7, 8, 3]

list2=[]
for i in list_:
    if i < 0:
        list2.append(abs(i))
    else:
        list2.append(i*(-1))


print(list2)