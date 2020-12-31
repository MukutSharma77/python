'''Write a Python program to combine two given sorted lists.
Original sorted lists:
[1, 3, 5, 7, 9, 11]
[0, 2, 4, 6, 8, 10]
After merging the said two sorted lists:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]'''


lst1=[1, 3, 5, 7, 9, 11]
lst2=[0, 2, 4, 6, 8, 10]
lst3=lst1+lst2
print(sorted(lst3))