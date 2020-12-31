# Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.

list_= [1, 6, 4, 7, 8]
count=0
for i in list_:
    product=1
    for j in list_:
        product=i*j
        if product % 2 != 0:
            print(True)
            count+=1
            break
    if count==1:
        break
if count==0:
    print(False)
