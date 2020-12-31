#Please print the Fibonacci Sequence in comma separated form with a given n input by console.

#Inputing number
num=int(input("Enter number :   "))

a=0
b=1
print(a,end="  ")
print(b,end="  ")

#running loop range 2 to num starting from 2 as already 2 are printed
for i in range(2,num):
    temp=a+b
    print(temp,end="  ")
    a=b
    b=temp
