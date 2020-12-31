# accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.

# enter binary number comma seprated
binary=input("Enter Binary number's (Commo seprated)    :  ").split(",")
list_=[]

#Checking is it divisble by 5 or not

for i in binary:
    # i = int(i)
    if int(i) % 5 == 0:
       list_.append(i)


print((',').join(list_))