#Python program to check the given year is a leap year or not

#inputting year to know leap or not
year=int(input("Enter year :    "))

if year % 4==0 or year % 400==0:
    print("Its leap year")
else:
    print("Not a leap year")