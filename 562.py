'''Inputting List by User'''

length=int(input("Enter Length Of a List :   "))
lst=[]
for i in range(1,length+1):
    x=input(f"Enter Element {i}   :    ")
    lst.append(x)

print(lst)