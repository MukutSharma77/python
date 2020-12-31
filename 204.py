'''Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
and than delete first and last element than display remaing element'''

#Input list :
color_list = ["Red","Green","White" ,"Black"]

print("The First element is :  ",color_list[0])
print("The Last element is :  ",color_list[-1])

#Deletion first and last element
color_list.remove(color_list[0])

color_list.remove(color_list[-1])

print("After Deleting list is ;   ",color_list)