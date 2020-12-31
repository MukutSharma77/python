'''Derivative of a Function
Create a function that takes numbers b and m as arguments and returns the derivative of the function f(x)=x^b with respect to x evaluated at x=m, where b and m are constants.
Examples
derivative(1, 4) ➞ 1
derivative(3, -2) ➞ 12
derivative(4, -3) ➞ -108
Notes
b * m ** (b – 1)'''


def derivative(b,m):
    print(b * m ** (b-1))

derivative(1, 4)
derivative(3, -2)
derivative(4, -3)
