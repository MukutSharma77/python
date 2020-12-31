'''Find the Unique Letters
Create a function that takes a string and returns the letters that occur only once.
Examples
find_letters("monopoly") ➞ ["m", "n", "p", "l", "y"]
find_letters("balloon") ➞ ["b", "a", "n"]
find_letters("analysis") ➞ ["n", "l", "y", "I"]'''

string="balloon"
list_=[i for i in string if string.count(i)==1]
print(list_)