'''Write a Python program to calculate the product of the unique numbers of a given list.
Original List : [10, 20, 30, 40, 20, 50, 60, 40]
Product of the unique numbers of the said list: 720000000
'''

list_=[10, 20, 30, 40, 20, 50, 60, 40]
list_=list(set(list_))

product=1
for i in list_:
    product*=i

print(product)