'''Is it Time for Milk and Cookies?
Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
Examples
time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True
time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False
time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True'''


import datetime
year=2013
month= 1
date= 23
string=datetime.date(year,month,date)
print('12-24' in str(string))