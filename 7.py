# Print all Numbers in a Range Divisible by a Given Number

#Inputting a number
num=int(input("Enter number :    "))


#loop to check is thi number is divisble by num
i=1
while i <= num:
    if num % i== 0:
        print(i,end=" , ")

    else:
        pass

    i+=1