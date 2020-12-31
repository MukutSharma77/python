#Count the Number of Digits in a Number

#Inputting number

num=int(input("Enter a number :  "))


#Counting Number of Digit in a given number
count=0
for i in str(num):
       count+=1

print(f"number of digit in{num} is :  ",count)