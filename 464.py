'''Armstrong'''

num=153
num_=num
tot=0

while num:
    mod=num % 10
    tot+=mod**3
    num=num//10

if tot==num_:
    print(True)
else:
    print(False)