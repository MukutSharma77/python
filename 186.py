'''Write a function that takes a year and returns its corresponding century.
Examples
century_from_year(2005) ➞ 21
(year + 99) // 100'''


#inputting year

year=int(input("Enter Year  :    "))
centuary=(year + 99) // 100

print('Centuary :   ',centuary)