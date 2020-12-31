'''Check if a String is a Mathematical Expression
Create a function that takes an input (e.g. "5 + 4") and returns True if it's a mathematical expression or False if not.
Examples
math_expr("4 + 5") ➞ True
math_expr("4*6") ➞ True
math_expr("4*no") ➞ False'''

def math_expr(string):
    try:
        string=string.replace(" ",'')
        num=eval(string)
        print(True)

    except Exception:
        print(False)


math_expr("4 + 5")
math_expr("4*6")
math_expr("4*no")