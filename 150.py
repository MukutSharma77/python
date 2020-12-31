#Python program for compound interest
'''
A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed
'''

p=float(input("initial principal balance   :    "))
r=float(input("interest rate :   "))
n=int(input('number of times interest applied per time period  :    '))
t=float(input("number of time periods elapsed :   "))

a=p*(1 + (r/n))**(n*t)
print(a)