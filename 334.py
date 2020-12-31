'''Create a function that takes a list of numbers or letters and returns a string.
Examples
list_to_string([1, 2, 3, 4, 5, 6]) ➞ "123456"
list_to_string(["a", "b", "c", "d", "e", "f"]) ➞ "abcdef"
'''

list_=[1, 2, 3, 4, 5, 'A']
string_=""
for i in list_:
    string_+=str(i)

print(string_)