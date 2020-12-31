#factorial of a given numbers.

#inputting a number

num=int(input("Enter Number :    "))

#Calculating factorial
tot=1
for i in range(1,num+1):
    tot*=i
    print(i,end="  ")
    if i == num:
        print(" = ",end=" ")
    else:
        print(" * ",end=" ")

print(tot)