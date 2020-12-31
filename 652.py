'''Find the Odd Integer
Create a function that takes a list and finds the integer which appears an odd number of times.
Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10'''

def find_odd(lst):
    num_=0
    for i in lst:
        if lst.count(i) % 2 !=0:
            num_=i
    print(num_)


lst=[10]
find_odd(lst)