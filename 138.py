#Python program to check whether a given number is a Fibonacci number or not

#inputing number
num=int(input("Enter number :   "))



if  num >= 0:
    a=0
    b=1
    i=0
    count=0
    #if input number is equal to Febancii seq number than it is else no
    while i<=num:
        c=a+b
        a=b
        b=c
        if num==c:
           print("Yes")
           count+=1
        i+=1




else:
    print("Invalid number")

if count==0:
    print("Not a febannaci number")
else:
    pass