'''Create a function that returns True if the first list can be nested inside the second.
list1 can be nested inside list2 if:
list1's min is greater than list2's min.
list1's max is less than list2's max.
Examples
can_nest([1, 2, 3, 4], [0, 6]) ➞ True
can_nest([3, 1], [4, 0]) ➞ True
can_nest([9, 9, 8], [8, 9]) ➞ False
can_nest([1, 2, 3, 4], [2, 3]) ➞ False'''

def can_nest(list1,list2):
    if min(list1) > min(list2) and max(list2) > max(list1):
        print(True)
    else:
        print(False)



list1=[ 1, 2, 3, 4 ]
list2=[2,3]
can_nest(list1,list2)