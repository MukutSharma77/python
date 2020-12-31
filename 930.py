''' Write a Python program to print a dictionary in table format
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
C1   C2    C3
1    5     9
2    6    10
3    7    11'''

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

key_=[i for i in my_dict.keys()]

val_=[i for i in my_dict.values()]



for i in key_:
    print(i,end="    ")
print()
for i in range(len(val_)):
    for j in range(len(val_[i])):
        print(val_[j][i],end="     ")
    print()
