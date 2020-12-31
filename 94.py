#Please write a program using generator to print the numbers
# which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

#In function we have a loop and condition that is chaecking is i is divisble by 5 an d 7
def check(num):
    for i in range(0,num):
        if i % 5 ==0 and i % 7 == 0:
            yield i

#inputting number
num=int(input("input Enter Number :   "))

#Fetchinhg value from yield 
for i in check(num):
    print(i,end=" ")
