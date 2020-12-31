# Calculate the Average of Numbers in a List


#Fuction For inputting list
def ele(no):
    list_=[ ]
    for i in range(1,no+1):
        x=int(input(f"Enter Element {i}   :     "))
        list_.append(x)

    return list_


# Inputting List And Calling the function
no=int(input("Enter Length of a List :   "))
result_list=ele(no)


#Printing List and Avg
print("\nThe List is :  ",result_list)

print("The Averge of a list is :  ",sum(result_list) / len(result_list))