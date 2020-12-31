'''Recursion to Repeat a String n Number of Times
Create a recursive function that takes two parameters and repeats the string n number of times. The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.
Examples
repetition("ab", 3) ➞ "ababab"
repetition("kiwi", 1) ➞ "kiwi"
repetition("cherry", 2) ➞ "cherrycherry"'''

def repetation(string,n):
    return string*n

string='cherry'
num=2
output=repetation(string,num)
print(output)