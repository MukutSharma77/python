'''Python program to find the maximum occurrence of a number in list'''

list_=[5,2,2,2,2,2,1,1,1,4,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

max_occ=list_.count(list_[0])
c=list_[0]
for i in list_:
    if max_occ < list_.count(i):
        max_occ=list_.count(i)
        c=i
print(c , ' is ' ,  max_occ , ' Times')
