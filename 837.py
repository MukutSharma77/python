'''837)Friday the 13th
Given the month and year as numbers, return whether that month contains a Friday 13th.
Examples
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False
'''
# import calendar:
import datetime
def has_friday_13(month,year):
    date_=datetime.date(year,month,13)
    print(date_.weekday()==4)

has_friday_13(3, 2020)
has_friday_13(10, 2017)
has_friday_13(1, 1985)
