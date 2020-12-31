'''Write a Python program to find all the values in a list are greater than a specified number.
check([220, 330, 500],200)
check([12, 17, 21],25)
output:
True
False
'''

def check(lst,num):
    count=0
    for i in lst:
        if i>=num:
            count+=1

    print(count==len(lst))


check([220, 330, 500],200)
check([12, 17, 21],25)