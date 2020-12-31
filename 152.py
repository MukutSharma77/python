#Find the sum of all numbers below 1000 which are multiples of 3 or 5

#Loop from u to 1000 and checking that which are multiples of 3 or 5 adding all that values

tot=0
for i in range(0,1001):
    if i % 3==0 or i % 5==0:
        tot+=i
    else:
        pass

print(tot)