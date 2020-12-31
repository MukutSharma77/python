'''Write a Python program to generate a number in a specified range except some specific numbers.
Generate a number in a specified range (1, 10) except [2, 9, 10]
7
Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
-4'''

import random
except_lst=[2,9,10]
lst_=random.choice([i for i in range(1,10) if i not in except_lst])
print(lst_)
