'''Your task is to create a function that takes a string, transforms all but the last four characters into "#" and returns the new masked string.
Examples
maskify("4556364607935616") ➞ "############5616"
maskify("64607935616") ➞ "#######5616"'''

def maskify(number):
    number=str(number)
    print("#" * (len(number)-4),end="")
    print(number[-4:])

number=64607935616
maskify(number)