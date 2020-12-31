'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
#Inporting module calender
import calendar

year=int(input("Enter year :   "))
month=int(input("Enter Month  :  "))

print(calendar.month(year,month))