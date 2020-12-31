'''Factor Chain
A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain:
[3, 6, 12, 36]
# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36
Create a function that determines whether or not a list is a factor chain.
Examples
factor_chain([1, 2, 4, 8, 16, 32]) ➞ True
factor_chain([1, 1, 1, 1, 1, 1]) ➞ True
factor_chain([2, 4, 6, 7, 12]) ➞ False
factor_chain([10, 1]) ➞ False'''

lst_=[10,1]


c=0
for i in range(len(lst_)-1):
    if lst_[i+1] % lst_[i]==0:
        c+=1

print(c==len(lst_)-1)
