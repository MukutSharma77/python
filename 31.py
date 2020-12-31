'''numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200'''

#Empty list and appending element which is divisible by 7 but are not a multiple of 5, between 2000 and 3200
list_=[]
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 !=0:
        list_.append(str(i))


# printing appending list
x=(",").join(list_)
print(x)