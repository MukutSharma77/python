#Write a Python program to check whether lowercase letters exist in a string

name='MUKUT'
count=0
for i in name:
    if i.islower():
        print(True)
        count+=1

if count==0:
    print(False)
