'''
We reverse 123 to get 321 and then add 123 to the end, resulting in 321123.

Examples
reverse_and_not(123) ➞ 321123

reverse_and_not(152) ➞ 251152'''



num=123

num=str(num)

print(num[::-1]+str(num))