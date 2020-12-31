'''Write two functions:
first_arg() should return the first parameter passed in.
last_arg() should return the last parameter passed in.
Examples
first_arg(1, 2, 3) ➞ 1
last_arg(1, 2, 3) ➞ 3'''


def first_arg(list):
    print(list[0])

def last_arg(list):
    print(list[-1])


list=[1,2,3]
first_arg(list)
last_arg(list)