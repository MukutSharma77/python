'''Write a Python program to count integer in a given mixed list.
Original list:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of integers in the said mixed list:
6'''

list_=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
int_count=0
for i in list_:
    if type(i)==int:
        int_count+=1

print(int_count)