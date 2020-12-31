'''Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
Examples
get_abs_sum([2, -1, 4, 8, 10]) ➞ 25
get_abs_sum([-3, -4, -10, -2, -3]) ➞ 22
get_abs_sum([2, 4, 6, 8, 10]) ➞ 30'''

def get_abs_(list_):
    tot=0
    for i in list_:
        tot+=abs(i)

    print(tot)


list_=[2, -1, 4, 8, 10]
get_abs_(list_)