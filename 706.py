'''Valid Division
Create a function that takes a division equation d and checks if it will return a whole number without decimals after dividing.
Examples
valid_division("6/3") ➞ True
valid_division("30/25") ➞ False
valid_division("0/3") ➞ True
Notes
Return "invalid" if division by zero.
'''

try:
    string="0/3"
    string=string.replace('/','%')
    print(eval(string)==0)
except Exception as e:
    print("invalid")