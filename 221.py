'''Write a Python program to convert height (in feet and inches) to centimeters.'''

print("1)   Feet to Centimeter \t 2)    Inches to Centimeter")

choose=int(input("Choose :   "))

if choose==1:
    print("Feet to Centimeter")
    f=float(input("Enter Feet :   "))
    print(f"{f} To Centimeter is :   {(f* 30.48).__round__(2)}")


elif choose==2:
    print("Inches to Centimeter")
    i=float(input("Enter Inches :   "))
    print(f"{i} To Centimeter is :   {(i * 2.54).__round__(2)}")

else:
    print("Invalid input")