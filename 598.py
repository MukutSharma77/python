'''Neatly Formatted Math
Given a simple math expression as a string, neatly format it as an equation.
Examples
format_math("3 + 4") ➞ "3 + 4 = 7"
format_math("3 - 2") ➞ "3 - 2 = 1"
format_math("4 x 5") ➞ "4 x 5 = 20"
format_math("6 / 3") ➞ "6 / 3 = 2"'''

expr=('6/3')
if '/'  in expr:
    expr=expr.replace('/','//')\

elif 'x' in expr:
    expr=expr.replace('x','*')


print(eval(expr))