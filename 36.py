#First Character and the Last Character have been Exchanged

#input String and then string letters appending in a list
string=input("Enter String :    ").split()
list_=[]
for i in string:
    for j in i:
        list_.append(j)

#Swapping first and last element
temp=list_[0]
list_[0] = list_[-1]
list_[-1]=temp


print(("").join(list_))