'''Return the Sum of the Two Smallest Numbers
Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
Examples
sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7
sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455
sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8
sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563
sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519'''

lst=[19, 5, 42, 2, 77]
lst_2=[i for i in lst if i > 0]
lst_2.sort()
print(lst_2[0]+lst_2[1])