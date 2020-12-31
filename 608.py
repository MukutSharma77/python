'''Magic Date
You are to read each part of the date into its own integer type variable. The year should be a 4 digit number. You can assume the user enters a correct date (no error checking required).
Determine whether the entered date is a magic date. Here are the rules for a magic date:
mm * dd is a 1-digit number that matches the last digit of yyyy or
mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
mm * dd is a 3-digit number that matches the last 3 digits of yyyy
The program should then display True if the date is magic, or False if it is not.
Examples
magic("1 1 2011") ➞ True
magic("4 1 2001") ➞ False
magic("5 2 2010") ➞ True
magic("9 2 2011") ➞ False'''

string="5 2 2010".split(" ")

if int(string[0]) * int(string[1])==int(string[2][-1]) or int(string[0]) * int(string[1])==int(string[2][-2:]) or int(string[0]) * int(string[1])==int(string[2][-3:]):
    print(True)
else:
    print(False)