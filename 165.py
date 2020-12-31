#Remove given number from list

list_=[1,2,3,4,5,6,7,8,9,10]

dlt=int(input("Delete Number :   "))

if dlt in list_:
    list_.remove(dlt)
    print(list_)

else:
    print("Not in a list")