'''Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.
Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6'''



def function(list_):
    list_tot=[]
    for i in list_:
        tot=0
        for j in str(i):
            j=int(j)
            tot+=j
            print(j,end=" ")
            i=str(i)
            if j==i[-1]:
                print(" = ",end=" ")
            else:
                print(" + ",end=" ")

        list_tot.append(tot)
        print(tot)
        print()

    if list_tot.count(list_tot[0])==len(list_tot):
        print(True)
    else:
        print(False)




list_=[105,33]
function(list_)