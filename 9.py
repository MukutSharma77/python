#########
#Accept Three Digits and Print all Possible Combinations from the Digits

#inputing 3 numbers
num1=int(input("Enter  Number1 :   "))
num2=int(input("Enter  Number2 :   "))
num3=int(input("Enter  Number3 :   "))

#given number in a list and inputting all input element
list_=[num1,num2,num3]
print("Three Input number :  ",end=" ")
for i in list_:
    print(i,end=" ")


#print all  possible combination 
for i in range(len(list_)):

    for j in range(len(list_)):

        for k in range(len(list_)):
            if i!=j and i!=k and j!=k:
                print(list_[i] , list_[j] ,list_[k])