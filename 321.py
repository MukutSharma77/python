'''Given a string of numbers separated by a comma and space, return the total of all the numbers.
Examples
add_nums("2, 5, 1, 8, 4") ➞ 20
add_nums("1, 2, 3, 4, 5, 6, 7") ➞ 28'''

num=input("Enter Number Comma seprated :  ").split(',')

tot=0
for i in num:
    tot+=int(i)

print(tot)