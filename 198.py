'''A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning
True if the integer is pandigital, and False otherwise.
'''

#inputting number and APPENDING unique number in a list
num=4567912345678123765241

list1=[]

for i in str(num):
    if int(i) not in list1:
        list1.append(int(i))

    list1.sort()


#Comparing pandigital list

list2=[1,2,3,4,5,6,7,8,9]

if list1==list2:
    print("Yes it is pandigital")

else:
    print("No the number is not pandigital")