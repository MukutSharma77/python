#Python Program to Put Even and Odd elements in a List into Two Different Lists


#Inputting list
list_=[1,2,3,4,5,10,9,8,7,6]

# checking each value of list if its even appending it in ev_list else odd_list

ev_list=[]
odd_list_=[]

for i in list_:
    if i % 2==0:
        ev_list.append(i)
    else:
        odd_list_.append(i)

print("All even value is :    ",ev_list)
print("All odd values is :    ",odd_list_)