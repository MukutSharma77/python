''' Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]'''

lst1= ["Black", "Red", "Maroon", "Yellow"]
lst_2=["#000000", "#FF0000", "#800000", "#FFFF00"]

list_output=[]
for i  in range(len(lst1)):
    dict_={}
    dict_[lst1[i]]=lst_2[i]
    list_output.append(dict_)

print(list_output)
