'''Sum of Found Indexes
Create a function which takes in a list of numbers and a number to find. Return the sum of every index in the list which matches the chosen number.
Examples
sum_found_indexes([0, 3, 3, 0, 0, 3], 3) ➞ 8
# The number 3 was found at indexes 1, 2 and 5.
# 8 = 1 + 2 + 5
sum_found_indexes([1, 2, 3, 4, 5, 6], 3) ➞ 2
'''

list_=[0, 3, 3, 0, 0, 3]
no=int(input("Enter Number :  "))

if no in list_:
    tot=0
    count=0
    for i in list_:
        if i == no:
            tot+=count
        count+=1
print(tot)