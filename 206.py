'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn'''

#Inputting number
num=int(input("Enter Number :   "))

tot=0
num_=num
for i in range(3):
    tot+=num_
    num_=(num_*10)+num

print(tot)