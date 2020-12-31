'''Write a function that does the following things: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge, the variable will be defined for you. All you have to do is look at the variable, do some string to integer conversions use some if conditionals, and combine them based on the operation.
The numbers and operation will be given as a string, and you should return the value as a string as well.
Examples
operation("1", "2", "add" ) ➞ "3"
operation("4", "5", "subtract") ➞ "-1"
operation("6", "3", "divide") ➞ "2"'''

def operation(num1,num2,sign):
    if sign=='add':
        print(f'"{str(int(num1) + int(num2))}"')
    elif sign=='subtract':
        print(f'"{str(int(num1) - int(num2))}"')

    elif sign=='divide':
        print(f'"{str(int(num1) // int(num2))}"')


operation("1", "2", "add" )
operation("4", "5", "subtract")
operation("6", "3", "divide")
