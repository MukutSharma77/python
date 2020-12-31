'''Write a function to make a list and in that there should be prime number within given range'''

def prime_lst(num1,num2):
    lst=[]

    for i in range(num1 , num2):
       for j in range(2,i):
            if i % j==0:
                break
       else:
           lst.append(i)

    print(lst)



prime_lst(1,20)