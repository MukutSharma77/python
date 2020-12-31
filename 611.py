'''List Operation
Create a function that takes three parameters and returns a list with the first parameter x, the second parameter y, and every number in between the first and second parameter in ascending order. Then filter through the list and return the list with numbers that are only divisible by the third parameter n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
Notes
The final list should consist of all numbers between x and y inclusive that are divisible by n.'''

start=15
end=20
div_by=7

lst=[]
for i in range(start,end+1):
    if i % div_by==0:
        lst.append(i)

print(lst)