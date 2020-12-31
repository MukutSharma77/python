'''Create a function that returns True if all parameters are truthy, and False otherwise.
Examples
all_truthy(True, True, True) ➞ True
all_truthy(True, False, True) ➞ False
all_truthy(5, 4, 3, 2, 1, 0) ➞ False'''

list_=[True, True, True]

if list_.count(list_[0]) == len(list_):
    print(True)
else:
    print(False)