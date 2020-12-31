'''Recreating a len() Function
Create a function which returns the length of a string, without using len().
Examples
length("Hello World") ➞ 11
length("Edabit") ➞ 6
length("wash your hands!") ➞ 16'''


string='wash your hands!'

count=0
for i in string:
    count+=1

print(count)