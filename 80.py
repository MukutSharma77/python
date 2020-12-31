#   Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

#Inputting number
no=int(input("Enter Number :   "))


# using loop and deviding i/(i+1) and adding it
tot=0
for i in range(1,no+1):
    tot=tot + float(i/(i+1))

    print(f"{i}/{i+1}",end=" ")
    if i==no:
        print(" = ",tot.__round__(2))
    else:
        print(" + ",end=" ")

