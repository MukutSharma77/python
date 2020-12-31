'''Create a function that takes a variable number of arguments, each argument representing the number of items in a group, and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
Examples
combinations(2, 3) ➞ 6
combinations(3, 7, 4) ➞ 84
combinations(2, 3, 4, 5) ➞ 120'''

def combinations(*args):
    tot=1
    for i in args:
        if i != 0:
            tot*=i

    print(tot)



combinations(2, 3)
combinations(3, 7, 4)
combinations(2, 3, 4, 5)