'''Sum of Cubes
Create a function that takes a list of numbers and returns the sum of its cubes.
Examples
sum_of_cubes([1, 5, 9]) ➞ 855
# Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855'''

list_=[1,5,9]
tot=0
for i in list_:
    tot+=i**3

print(tot)