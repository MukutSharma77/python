#Print Odd Numbers Within a Given Range

#inputting number

num=int(input("Enter Number :   "))

#Checking and all odd number from 0 to N

i=1

while i<=num:
    if i%2!=0:
        print(i,end="  ")

    else:
        pass
    i+=1