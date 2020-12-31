'''
Write a Python program to extract common index elements from more than one given list.
Original lists:
[1, 1, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 7]
[0, 1, 2, 3, 4, 5, 7]
Common index elements of the said lists:
[1, 7]
'''

nums1 = [1, 1, 3, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 5, 7]
nums3 = [0, 1, 2, 3, 4, 5, 7]

lst_common=[]
for m , n , o in zip(nums1,nums2,nums3):
    if m==n==o:
        lst_common.append(m)
print(lst_common)
