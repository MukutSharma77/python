'''Count Instances of a Character in a String
Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
Examples
char_count("a", "edabit") ➞ 1
char_count("c", "Chamber of secrets") ➞ 1'''


string="Chamber of secrets"
count=input("Comnt :  ")

if count in string:
    print(string.count(count))

else:
    print("0")