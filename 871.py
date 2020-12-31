'''

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

#
#
#
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end=" ")
#         j+=1
#     print()
#     i+=1
#
# i=4
# while i>=1:
#     j=i
#     while j >= 1:
#         print("*",end=" ")
#         j-=1
#     print()
#     i-=1


for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

for i in range(4,0,-1):
    for j in range(i,0,-1):
        print('*',end=" ")
    print()