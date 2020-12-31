'''Compare Strings by Count of Characters
Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
Examples
comp("AB", "CD") ➞ True
comp("ABC", "DE") ➞ False
comp("hello", "edabit") ➞ False'''

str1='AB'
str2='CD'
print(len(str2)==len(str1))