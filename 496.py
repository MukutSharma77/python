'''Fix the Error: Mutating Arrays
Suppose I want to define a function that removes the last element of a list each time I call it, but does not mutate the original list. Fix the code so that the results are no longer mutating the list.
x = [1, 2, 3, 4, 5]
minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
minus_one(x) ➞ [1, 2, 3]  # 2nd time function is called.
minus_one(x) ➞ [1, 2]  # 3rd time function is called.
minus_one(x) ➞ [1]  # 4th time function is called.'''

list_=[1,2,3,4,5]

for i in range(0,len(list_)):
    print(list_)
    list_.pop()