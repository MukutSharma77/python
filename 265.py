y'''Create a function that takes a string and censors words over four characters with *.
Examples
censor("The code is fourty") ➞ "The code is ******"
censor("Two plus three is five") ➞ "Two plus ***** is five"
'''

string="Two plus three is five"

string=string.split(" ")
for i in string:
    if len(i) > 4:
        print('*' * len(i),end=" ")
    else:
        print(i,end=" ")