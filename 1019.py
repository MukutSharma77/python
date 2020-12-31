'''Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list.
The original list, tuple :
[(2, 7), (2, 6), (1, 8), (4, 9)]
Maximum and minimum product from the pairs of the said tuple of list:
(36, 8)'''

list_=[(2, 7), (2, 6), (1, 8), (4, 9)]
max_product=0
min_product=list_[0][0] * list_[0][1]
for i in list_:
    tot=1
    for j in i:
        tot*=j
    # print(tot)
    if tot>max_product:
        max_product=tot

    elif tot<min_product:
        min_product=tot

print((max_product,min_product))
