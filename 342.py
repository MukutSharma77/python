'''Given two unique integer lists a and b, and an integer target value v, create a function to determine whether there is a pair of numbers that add up to the target value v, where one number comes from one list a and the other comes from the second list b.
Return True if there is a pair that adds up to the target value and False otherwise.
Examples
sum_of_two([1, 2], [4, 5, 6], 5) ➞ True
sum_of_two([1, 2], [4, 5, 6], 8) ➞ True
sum_of_two([1, 2], [4, 5, 6], 3) ➞ False'''


def sum_of_two(list1_,list2_,num):
    count=0
    if len(list2_) > len(list1_):
        for i in list2_:
            for j in list1_:
                if i + j==num:
                    print(True)
                    count+=1
        if count==0:
            print(False)

    else:
        for i in list1_:
            for j in list2_:
                if i + j == num:
                    print(True)
                    count += 1
        if count == 0:
            print(False)


list1_=[1,2]
list2_=[4,5,6]
num=int(input("Enter number :  "))
sum_of_two(list1_,list2_,num)