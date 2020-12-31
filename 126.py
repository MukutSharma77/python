#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

import random

#Creating emopty list
list_=[]

#appending random 1 to 20 till length of list is not 20
while True:
    random_val=random.randint(1,20)
    if random_val not in list_:
        list_.append(random_val)

    elif len(list_)==20:
        break

    else:
        pass

print(list_)
