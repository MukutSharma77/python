'''Write a Python program to convert a given tuple of positive integers into an integer.
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123'''

tup=(1,2,3)
int_num=''
for i in tup:
    int_num+=str(i)

print(int(int_num))