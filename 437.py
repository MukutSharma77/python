'''Modifying the Last Character
Create a function which makes the last character of a string repeat n number of times.
Examples
modify_last("Hello", 3) ➞ "Hellooo"
modify_last("hey", 6) ➞ "heyyyyyy"
modify_last("excuse me what?", 5) ➞ "excuse me what?????"'''

string='hey'
time=3
print(string[:-1] + string[-1] * time)