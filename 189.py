#python program to check given given number is niven number or not


#Inputtimng number
num=int(input("Enter Number :   "))

#Calculating sum of digit
sum_of_digit=0

for i in str(num):
    sum_of_digit+=int(i)

#Checking is the number is miven or not

if num % sum_of_digit==0:
    print("Yes the number is nivem")
else:
    print("No the number is not a niven")
