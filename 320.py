'''Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.
Examples
operation(15, 9) ➞ "added"
operation(26, 2) ➞ "subtracted"
operation(11, 11) ➞ None
'''

def function(num1,num2):
    if num1+num2==24 :
        return 'Added'

    elif num1-num2==24 :
        return 'Subtract'


    elif num1*num2==24 :
        return 'Multiplication'

    elif num1//num2==24:
        return 'Devided'
    else:
        return None


num1=int(input("Enter Number 1 :  "))
num2=int(input("Enter Number 2 :  "))
result=function(num1,num2)
print(result)