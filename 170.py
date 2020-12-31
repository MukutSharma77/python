# Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n
'''Case 1:
Enter the number of terms:3
Enter the value of x:1
The sum of series is 1.83'''



n=int(input("Enter Numbeer :    "))
x=int(input("Enter X   :      "))
tot=1

for i in range(2,n+1):
    tot+=(x**i)/i

print(tot.__round__(2))