'''Total Number of Unique Characters
Given two strings, create a function that returns the total number of unique characters from the combined string.
Examples
count_unique("apple", "play") ➞ 5'''

string1=input("Enter string1 :  ")
string2=input("Enter string2 :  ")

count=set(string2+string1)
print(len(count))