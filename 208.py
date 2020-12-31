'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

#IMPORTING DATE TIME

import datetime

year1=datetime.date(2014, 7, 2)
year2=datetime.date(2014, 7, 11)

print("The number of days between 2 dates are  :     ",abs(year1-year2))