'''Make My Way Home
You will be given a list, showing how far James travels away from his home for each day. He may choose to travel towards or away from his house, so negative values are to be expected.
Create a function which calculates how far James must walk to get back home.
Examples
distance_home([2, 4, 2, 5]) ➞ 13
distance_home([-1, -4, -3, -2]) ➞ 10
distance_home([3, 4, -5, -2]) ➞ 0'''

list_=[3, 4, -5, -2]
print(abs(sum(list_)))