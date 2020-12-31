'''Stupid Addition
Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
Examples
stupid_addition(1, 2) ➞ "12"
stupid_addition("1", "2") ➞ 3
stupid_addition("1", 2) ➞ None
'''

def stupid_addition(num1,num2):
    if type(num1)==int and type(num2)==int:
        print(str(num1)+str(num2))
    elif type(num1)==str and type(num2)==str:
        print(int(num1)+int(num2))

    else:
        print(None)

stupid_addition(1, 2)
stupid_addition("1", "2")
stupid_addition("1", 2)
