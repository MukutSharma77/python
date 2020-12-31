'''Is There an Upward Trend?
Create a function that determines if there is an upward trend.
Examples
upward_trend([1, 2, 3, 4]) ➞ True
upward_trend([1, 2, 6, 5, 7, 8]) ➞ False
upward_trend([1, 2, 3, "4"]) ➞ "Strings not permitted!"
upward_trend([1, 2, 3, 6, 7]) ➞ True'''

lst=[1, 2, 3, 6, 7]

count=0
for i in lst:
    if type(i)==str:
        print("Strings not permitted")
        count+=1

if count==0:
    print(lst==sorted(lst))

