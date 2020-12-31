'''Write a Python program to compute the sum of digits of each number of a given list.
sum_( [10, 2, 56] )
sum_( [10, 20, 4, 5, 'b', 70, 'a'] )
sum_( [10, 20, -4, 5, -70])
Output :
14
19
19'''

def sum_(lst):
    tot=0
    for i in lst:
        if type(i)==int:
            i=str(i).replace('-','')
            for k in i:
                tot+=int(k)

    print(tot)


sum_( [10, 2, 56] )
sum_( [10, 20, 4, 5, 'b', 70, 'a'] )
sum_( [10, 20, -4, 5, -70])
