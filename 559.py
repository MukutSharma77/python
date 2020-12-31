'''Return Odd > Even
Given a list, return True if there are more odd numbers than even numbers, otherwise return False.
Examples
oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ True
oddeven([1]) ➞ True
oddeven([13452394823795273847528572346]) ➞ False'''

def oddeven(lst):
    tot_ev=0
    tot_odd=0
    for i in lst:
        if i % 2==0:
            tot_ev+=1
        else:
            tot_odd+=1

    return tot_odd > tot_ev


lst=[1]
output=oddeven(lst)
print(output)