'''
385)Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:
Total number of slices.
Number of recipients.
How many slices each person gets.
The function will be in this form:
equal_slices(total slices, no. recipients, slices each)
Examples
equal_slices(11, 5, 2) ➞ True
# 5 people x 2 slices each = 10 slices < 11 slices
equal_slices(11, 5, 3) ➞ False
# 5 people x 3 slices each = 15 slices > 11 slices
'''

tot=int(input("Total number of slices  :       "))
person=int(input("Total number of person  :    "))
person_get=int(input("No of slices pereson gets :   "))

if person*person_get < tot:
    print(True)
else:
    print(False)
