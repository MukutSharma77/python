# Find the Smallest Divisor of an Integer


#Inputting a number
num=int(input("Enter Number :   "))

#Using loop nto check smaller divisor

i=2
if num >= 2:
    while i <= num:
        if num % i == 0:
            print("The smallest Divisor is :  ",i)
            break

        else:
            pass

        i+=1