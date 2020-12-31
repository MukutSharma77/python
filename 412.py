'''Product of All Odd Integers
Create a function that returns the product of all odd integers in a list.
Examples
odd_product([3, 4, 1, 1, 5]) ➞ 15
odd_product([5, 5, 8, 2, 4, 32]) ➞ 25
odd_product([1, 2, 1, 2, 1, 2, 1, 2]) ➞ 1'''


list_=[5, 5, 8, 2, 4, 32]

sum=1
for i in list_:
    if i % 2!=0:
        sum*=i

print(sum)