'''Given a list of integers, replace every number with the average mean of the whole list.
Examples
flatten_the_curve([1, 2, 3, 4, 5]) ➞ [3, 3, 3, 3, 3]
flatten_the_curve([0, 0, 0, 2, 7, 3]) ➞ [2, 2, 2, 2, 2, 2]'''

list_=[1, 2, 3, 4, 5]

avg=sum(list_)/len(list_)
listing=[int(avg) for i in range(len(list_))]
print(listing)