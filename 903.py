'''Write a Python script to sort (ascending and descending) a dictionary by value.'''

dict_={
    1:5,
    2:2,
    3:9,
    4:1
}
print("Dictionary :  ",dict_)
sorted_val=sorted(dict_.values())
lst_val=[i for i in dict_.values()]


dict_2={}

for i in sorted_val:
    for k in dict_.keys():
        if dict_[k]==i:
            dict_2[k]=i




print('Ascending order :   ',dict_2)

sorted_val.reverse()
dict_3={}
for i in sorted_val:
    for j in dict_.keys():
        if dict_[j]==i:
            dict_3[j]=i

print('Desceding order :  ',dict_3)