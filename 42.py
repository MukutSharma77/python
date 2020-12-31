#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.


#Input number
num=int(input("Enter Number :   "))

number=num
tot=0

#loop for 5 times to add a + aa + aaa +aaaa
for i in range(1,5):
    tot+=number
    number =  (number * 10) + num

print(tot)