'''How Many Solutions Does This Quadratic Have?
A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.
Examples
solutions(1, 0, -1) ➞ 2
// x² - 1 = 0 has two solutions (x = 1 and x = -1).
solutions(1, 0, 0) ➞ 1
// x² = 0 has one solution (x = 0).
solutions(1, 0, 1) ➞ 0
// x² + 1 = 0 has no solutions'''


a=1
b=0
c=-1
formula=(b**2)-(4*a*c)

if formula > 0:
    print(2)

elif formula==0:
    print(1)

else:
    print(0)