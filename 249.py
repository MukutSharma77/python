#Days in a Month.py

month=int(input("Enter Number :   "))

if month==1:
    print("total number of days 31")


elif month==2:
    year=int(input("Enter Year :  "))
    if year%4==0 or year%400==0:
        print("total number of days 29")
    else:
        print("Total number of days 28")

elif month==3:
    print("total number of days 31")

elif month==4:
    print("total number of days 30")


elif month == 5:
    print("total number of days 31")


elif month == 6:
    print("total number of days 30")


elif month == 7:
    print("total number of days 31")


elif month == 8:
    print("total number of days 30")



elif month == 9:
    print("total number of days 30")


elif month == 10:
    print("total number of days 31")


elif month == 11:
    print("total number of days 30")


elif month == 12:
    print("total number of days 31")

else:
    print("Invalid ")

