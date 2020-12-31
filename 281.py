'''

Create a function that takes an integer n and returns the nth tetrahedral number.
 (n * (n + 1) * (n + 2)) / 6'''

output=lambda n : (n * (n + 1) * (n + 2)) / 6

n=int(input("Enter Number :   "))
result=output(n)
print(result)