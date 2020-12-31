#Ask the user for a number and determine whether the number is prime or not.

#Inputing number by user :
num=int(input("Enter Number :    "))

#Checking is it prime or not with loop
count=0
if num >=2 :
    for i in range(2,num):
        if num % i==0:
            count+=1
        else:
            pass

    if count == 0:
        print("Prime Number")
    else:
        print("Not a Prime Number")

else:
    print("Input nbumber is small")

