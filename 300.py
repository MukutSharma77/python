'''Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and
the second element is the sum of negative numbers.
Examples
sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
# There are a total of 10 positive numbers.
# The sum of all negative numbers equals -65.
'''

def function(list_):
    count=0
    sum_=0
    for i in list_:
        if i < 0:
            sum_+=i
        else:
            count+=1

    list2=[count,sum_]
    print(list2)



list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
function(list_)