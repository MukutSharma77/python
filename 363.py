'''Valid Variable Names
When creating variables, the variable name must always start with a letter and cannot contain spaces, though numbers and underscores are allowed to be contained in it also.
Create a function which returns True if a given variable name is valid, otherwise return False.
Examples
variable_valid("result") ➞ True
variable_valid("odd_nums") ➞ True
variable_valid("2TimesN") ➞ False'''

def variable_valid(string):
    if string[0] in '0123456789':
        print(False)
    elif string.isalpha() or '_' in string:
        print(True)



    else:
        print(False)



string=input("Enter String :   ")
variable_valid(string)