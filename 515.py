'''True Ones, False Zeros
Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
Examples
integer_boolean("100101") ➞ [True, False, False, True, False, True]
integer_boolean("10") ➞ [True, False]
integer_boolean("001") ➞ [False, False, True]'''

num='100101'
list_=[]
for i in num:
    if i=='1':
        list_.append(True)
    else:
        list_.append(False)

print(list_)