''')Transform Upvotes
Create a function that transforms a string of upvote counts into a list of numbers. Each k represents a thousand.
Examples
transform_upvotes("6.8k 13.5k") ➞ [6800, 13500]
transform_upvotes("5.5k 8.9k 32") ➞ [5500, 8900, 32]
transform_upvotes("20.3k 3.8k 7.7k 992") ➞ [20300, 3800, 7700, 992]'''

string=input("Enter comma seprated :   ").split(" ")
list2=[]
for i in string:
    if i[-1]=='k':
       i=i.replace('k','')
       i=float(i)*1000
       list2.append(int(i))
    else:
        list2.append(int(i))

print(list2)
