'''Difference of Max and Min Numbers in List
Create a function that takes a list and returns the difference between the biggest and smallest numbers.
Examples
difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.
difference_max_min([44, 32, 86, 19]) ➞ 67'''


list_=[10, 4, 1, 4, -10, -50, 32, 21]
print(max(list_) - min(list_))