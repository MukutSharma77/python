'''Even Odd Partition
Write a function that partitions the list into two sublists: one with all even integers, and the other with all odd integers. Return your result in the following format:
[[evens], [odds]]
Examples
even_odd_partition([5, 8, 9, 2, 0]) ➞ [[8, 2, 0], [5, 9]]
even_odd_partition([1, 0, 1, 0, 1, 0]) ➞ [[0, 0, 0], [1, 1, 1]]
even_odd_partition([1, 3, 5, 7, 9]) ➞ [[], [1, 3, 5, 7, 9]]
even_odd_partition([]) ➞ [[], []]
'''

list_=[5, 8, 9, 2, 0]
list_ev=[i for i in list_ if i%2==0]
list_od=[i for i in list_ if i%2!=0]
list3=[list_ev,list_od]
print(list3)