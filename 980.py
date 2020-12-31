''' Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]'''

list_=[1, 2, 3, 4, 5, 6, 7, 8, 9]
num=[]
for i in list_:
    for j in list_:
        if i!=j:
            if int(str(i)+str(j)) not in num:
                num.append(int(str(j)+str(i)))
                print([i,j],end="  ")
    print()
print(num)