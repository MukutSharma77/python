'''Unlucky Years
Create a function which returns how many Friday 13ths there are in a given year.
Examples
howUnlucky(2020) ➞ 2
howUnlucky(2026) ➞ 3
howUnlucky(2016) ➞ 1'''

import datetime
def howUnlucky(year):
    count=0
    for i in range(1,13):
        if datetime.date(year,i,13).weekday()==4:
            count+=1

    print(count)

howUnlucky(2020)
howUnlucky(2026)
howUnlucky(2016)