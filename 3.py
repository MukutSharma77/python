#Read a Number n and Compute n+nn+nnn

#Inputting number
num1=int(input("Enter Number   :    "))

tot=0
i=1
num_=num1

#Loop For Diplay n + nn + nnn....=TOTAL
while i <= num1:
    tot+=num_
    print(num_,end=" ")
    num_= num_ * 10 + num1
    if i == num1:
        print(' = ',end=" ")
    else:
        print(" + ",end=" ")
    i+=1

print(tot)
