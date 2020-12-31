'''print 1 to 50 number if the  umber is divisble by 3 and 5 than ignore that number'''
i=1

for i in range(1,51):
    if i % 3==0 or i%5==0:
        continue
    else:
        print(i,end="  ")