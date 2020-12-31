'''Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
Ex.: 8 = 73+63+53+43+33+23+13 = 784'''

num=int(input("Enter Number :    "))
list_=[]
tot=0
for i in range(1,num):
    tot+=i**3
    list_.append(i**3)

print(tot)