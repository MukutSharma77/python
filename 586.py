'''Only Evens!
create a function that returns True if the num is even and return False if the num is odd. But if the num type is float return None
Examples to use in code:
type(num) == type
num % odd_num == 0
Examples
odd_or_even(6)  ➞  True
odd_or_even(5) ➞  False
odd_or_even(3.2) ➞  None
'''

num=3.2

if type(num)==float:
    print(None)
elif num%2==0:
    print(True)
else:
    print(False)