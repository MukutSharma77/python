'''Number to Reversed Array
Create a function that takes a number and returns a list with the digits of the number in reverse order.
Examples:
reverse_list(1485979) ➞ [9, 7, 9, 5, 8, 4, 1]
reverse_list(623478) ➞ [8, 7, 4, 3, 2, 6]
reverse_list(12345) ➞ [5, 4, 3, 2, 1]'''

num=12345

num=(str(num))
num=num[::-1]


list1=[]
for i in num:
    list1.append(int(i))

print(list1)