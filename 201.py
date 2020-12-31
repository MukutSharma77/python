#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

#Inputting number
num=int(input("Enter Number :   "))

#17 - inputed number
dif=17-num

if num > 17:
    print("Dopubling the value  :    ",abs(dif)*2)
else:
    print("Abslout valuue :   ",abs(dif))