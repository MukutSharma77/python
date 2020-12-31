'''List of Multiples
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.
Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]'''

tab=12
till=10
lst=[]
for i in range(1,till+1):
    lst.append(tab*i)

print(lst)