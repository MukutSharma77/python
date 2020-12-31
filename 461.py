'''Get Word Count
Create a function that takes a string and returns the word count. The string will be a sentence.
Examples
count_words("Just an example here move along") ➞ 6
count_words("This is a test") ➞ 4
count_words("What an easy task, right") ➞ 5'''

string="This is a test".split(" ")
print(len(string))