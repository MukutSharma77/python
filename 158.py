# Find the sum of all prime numbers till 1000

tot=0
for i in range(2,1000):
    count=0
    for j in range(2,i):
        if i % j == 0:
           count+=1

    if count==0:
        tot+=i
    else:
        pass

print(tot)