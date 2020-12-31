'''Are Letters in the Second String Present in the First?
Create a function that accepts a list of two strings and checks if the letters in the second string are present in the first string.
Examples
letter_check(["trances", "nectar"]) ➞ True
letter_check(["compadres", "DRAPES"]) ➞ True
letter_check(["parses", "parsecs"]) ➞ False'''

lst=["parses", "parsecs"]

count=0
for i in lst[0].lower():
    if i in lst[1].lower():
        count+=1

print(count==len(lst[1]))