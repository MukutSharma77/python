'''
 Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''

sample_list=[ 'p' , 'q' ]
sample_num=5

lst=[]
for i in range(1,sample_num+1):
    for j in sample_list:
        lst.append(j + str(i))

print(lst)