'''Impossible Date
Given the parameters day, month and year, return whether that date is a valid date.
Examples
is_valid_date(35, 2, 2020) ➞ False
# February doesn't have 35 days.
is_valid_date(8, 3, 2020) ➞ True
# 8th March 2020 is a real date.
is_valid_date(31, 6, 1980) ➞ False
# June only has 30 days.'''

import datetime
def is_valid_date(dd,mm,yy):
    try:
        date_=datetime.date(yy,mm,dd)

        print(True)
    except Exception as e:
        print(False)


is_valid_date(35, 2, 2020)
is_valid_date(8, 3, 2020)
is_valid_date(31, 6, 1980)