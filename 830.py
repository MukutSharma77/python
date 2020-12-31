'''Adding Both Ends Together
Given a list of numbers, of any length, create a function which counts how many of those numbers pass the following criterea:
The first and last digits of a number must add to 10.
Examples
ends_add_to_10([19, 46, 2098]) ➞ 3
ends_add_to_10([33, 44, -55]) ➞ 1
ends_add_to_10([]) ➞ 0'''

def ends_add_to_10(lst):
    count=0
    for i in lst:
        i=str(i)
        i=i.replace('-','')
        if int(i[0]) + int(i[-1]) ==10:
            count+=1

    print(count)


ends_add_to_10([19, 46, 2098])
ends_add_to_10([33, 44, -55])
ends_add_to_10([])