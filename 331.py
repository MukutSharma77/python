'''Calculate Using String Operation
Create a function that takes two numbers and a mathematical operator and returns the result.
Examples
calculate(4, 9, "+") ➞ 13
calculate(12, 5, "-") ➞ 7
calculate(6, 3, "*") ➞ 18
calculate(25, 5, "//") ➞ 5'''


def calculate(cal):
    if cal[-1]=='+':
        print(cal[0] + cal[1])

    elif cal[-1]=='-':
        print(cal[0] - cal[1])


    elif cal[-1]=='*':
        print(cal[0] - cal[1])


    elif cal[-1]=='//':
        print(cal[0] // cal[1])

cal=[4,5,'-']
calculate(cal)