# Find the Sum of Digits in a Number

#Inputting Number

num=int(input("Enter Number :   "))

#using loop to do sum of digit in a input number
tot=0
for i in str(num):
    tot+=int(i)

print(f" Sum of Digits in a {num}   :    ",tot)