'''
Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. If the sum of the first half equals the sum of the second half, return the original list.
Examples
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1 sol = [6, 3, 1, 6, 3, 1]'''

list_=[1 ,2 , 4, 6, 3, 1]
new_list=[]

if sum(list_[0:len(list_)//2]) > sum(list_[len(list_)//2 : ]):
    new_list=list_[0:len(list_)//2]*2

elif sum(list_[0:len(list_)//2]) < sum(list_[len(list_)//2 : ]):
    new_list = list_[len(list_) // 2 :]*2

else:
    print("Same ")
    print(list_)


print(new_list)