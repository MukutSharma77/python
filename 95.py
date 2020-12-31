#Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

#in Function we have loop that is checking even number 0 to N
def even(num):
    for i in range(0,num+1):
        if i%2==0:
            yield i

#Inputting number and from loop fetching the yield value
num=int(input("Enter number :   "))

for i in even(num):
    print(i,end=" ")
