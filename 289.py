'''In this challenge you will be given a list of numbers. Your task is to "marry" each pair of adjacent numbers by adding them, and return the list of "couples" (i.e. sums).
If the list has an odd length, one number is (sadly) left out, so you should return "bad match".
Examples
is_good_match([1, 2, 4, 7]) ➞ [1+2, 4+7] ➞ [3, 11]
is_good_match([5, 7, 9, -1, 4, 2]) ➞ [12, 8, 6]
is_good_match([5, 7, 9, -1, 4, 2, 3]) ➞ "bad match"'''

def function(list_):
    if len(list_) % 2==0:
        list_1=[]
        for i in range(0,len(list_),2):
            list_1.append(list_[i]+list_[i+1])

        print(list_1)

    else:
        print("Bad match")

list_=[5, 7, 9, -1, 4, 2]
function(list_)