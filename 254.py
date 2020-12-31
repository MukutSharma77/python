'''
Create a function thats takes a list and returns True if every number is prime. Otherwise, return False.'''

#List
lists_=[2,3,5,7 ,11]
count_prime=0
for i in lists_:
    count=0
    if i >= 2:
        for j in range(2,i):
            if i % j==0:
                count+=1
            else:
                pass
        if count==0:
            count_prime+=1
        else:
            pass


if count_prime==len(lists_):
    print(True)
else:
    print(False)