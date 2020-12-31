#Python Program to Print Table of a Given Number

#inputting number by user
number=int(input("Enter Number :   "))

#using loop to print a table and multiple number * i
for i in range(1,11):
    print(f"{number}  *  {i}    =    {number*i}")