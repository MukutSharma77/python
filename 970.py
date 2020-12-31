''' Write a Python program to check whether all dictionaries in a list are empty or not
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False'''

def check(lst):
    count=0
    for i in lst:
        if type(i)==dict and i:
            pass
        elif type(i)==dict:
            count+=1

    print(count==len(lst))
check([{},{},{}])
check([{1,2},{},{}])