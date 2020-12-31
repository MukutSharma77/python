# Print an Inverted Star Pattern

#Inputing no of rows for inverted pattern
num=int(input("Enter number :   "))
print()

#using three loops one for row second for space third to print stars
for i in range(num,-1,-1):
    for space in range(i,num):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")

    print()