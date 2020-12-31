'''Remove Surrounding Duplicate Items
Create a function that takes a sequence of either strings or integers, removes the surrounding duplicates and returns a list of items without any items with the same value next to each other and preserves the original order of items.
Examples
unique_in_order("AAAABBBCCDAABBB") ➞ ["A", "B", "C", "D", "A", "B"]
unique_in_order("ABBCcAD") ➞ ["A", "B", "C", "c", "A", "D"]
unique_in_order([1, 2, 2, 3, 3]) ➞ [1, 2, 3]b '''

string="AAAABBBCCDAABBB"
# string_=[i for i in string]
# print(string_)
output=[string[0]]

for i in string:
    if i != output[-1]:
        output.append(i)
    else:
        pass



print(output)