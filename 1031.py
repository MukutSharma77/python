''' Write a Python program to find a first even and odd number in a given list of numbers.
Original list:
[1, 3, 5, 7, 4, 1, 6, 8]
First even and odd number of the said list of numbers:
(4, 1)'''

lst_=[1, 3, 5, 7, 4, 1, 6, 8]
even=[i for i in lst_ if i%2==0]
odd=[i for i in lst_ if i%2!=0]
print((even[0],odd[0]))
